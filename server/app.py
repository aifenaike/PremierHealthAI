import socketio
from flask import Flask
from model import diagnosis_report_writer, diffdiag_prompt, questions_prompt
from socketcallback import SocketIOCallback
from state import state_store
import logging
from socketcallback import SocketIOCallback
from concurrent.futures import ThreadPoolExecutor
import os
from transcribe_whisper import transcribe_whisper


## Path to medical_assiatant functinalities
import sys
sys.path.append('./medical_assistant')

from medical_assistant import medical_assistant
from inventory_assistant import inventory_agent
## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

sio = socketio.Server(cors_allowed_origins='*', async_mode='threading')
app = Flask(__name__)
app.wsgi_app = socketio.WSGIApp(sio, app.wsgi_app)
USE_WHISPER = os.getenv("USE_WHISPER", "true") == "true"


## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------
@sio.event
def connect(sid, env):
    print('connect ',  )


@sio.event
def disconnect(sid):
    print('disconnect ', sid)


@sio.event
def start_recording(sid, value):
    global state_store
    print('start recording ', sid)
    stop = transcribe_whisper(transcript_callback)
    state_store["stop"] = stop
    return True


@sio.event
def stop_recording(sid, value):
    global state_store
    print('stop recording ', sid)
    stop = state_store["stop"]
    stop(True)
    state_store["stop"] = None
    return True


@sio.event
def set_summary(sid, text):
    global state_store
    state_store["pharmacist_summary"] = text
    print('set_summary', sid, state_store["pharmacist_summary"])


@sio.event
def generate_notes(sid, pharmacist_hints):
    global state_store
    print("transcript for note generation", state_store["transcript"])
    print("pharmacist_hints", pharmacist_hints)
    steam_handler = SocketIOCallback(lambda x: sio.emit('generate_notes', x))
    notes = diagnosis_report_writer.run(
        {
            "pharmacist_hints": pharmacist_hints,
            "transcript": state_store["transcript"]
        },
        callbacks=[steam_handler])
    print("Generated notes", notes)
    sio.emit('generate_notes', notes, sid)

## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------
@sio.event
def patient_mode(sid, boolean):
    global state_store
    state_store["patient_mode"] = boolean
    print('patient_mode', sid, boolean)

@sio.event
def inventory_assistant_mode(sid, boolean):
    global state_store
    state_store["inventory_assistant_mode"] = boolean
    print('inventory_assistant_mode', sid, boolean)


## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------
@sio.event
def patient_recording(sid, boolean):
    global state_store
    state_store["patient_recording"] = boolean
    print('patient_recording', sid, boolean)


@sio.event
def inventory_assistant_recording(sid, boolean):
    global state_store
    state_store["inventory_assistant_recording"] = boolean
    print('inventory_assistant_recording', sid, boolean)

## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------
@sio.event
def patient_message(sid, text):
    print("[socket] received patient message", text)
    ai_response = medical_assistant.agent_executor.run(
        {
            "input": text,
        })
    sio.emit('patient_message', {
        "text": ai_response,
        "done": True
    }, sid)


@sio.event
def inventory_assistant_message(sid, text):
  
    ai_response = inventory_agent.run(text)
    
    sio.emit('inventory_assistant_message', {
        "text": ai_response,
        "done": True
    }, sid)


## --------------------------------------------------------------------------------------------------------------------
## --------------------------------------------------------------------------------------------------------------------

def send_transcript(text):
    sio.emit('transcript', text)


def send_patient_transcript(text):
    sio.emit('patient_transcript', text)


def send_ai_note(text):
    sio.emit('ai_note', text)


def send_cds_ddx(text):
    # print("[socket] sending cds ddx", text)
    sio.emit('cds_ddx', text)


def send_cds_qa(text):
    # print("[socket] sending cds qa", text)
    sio.emit('cds_qa', text)


def send_patient_instructions(text):
    sio.emit('patient_instructions', text)


def send_patient_audio_message(content):
    sio.emit('patient_audio_message', content)


def start_socketio_server():
    app.run('0.0.0.0', 5000)


ai_note_set = 0


def run_on_transcript(text, sendFn, chain):
    global ai_note_set
    print("[tread] running transcript", text)
    callbacks = None
    if ai_note_set < 2:
        callbacks = [SocketIOCallback(sendFn)]
        ai_note_set += 1
    print("[thread] runnin chain", text, sendFn, chain)
    final_result = chain.run({"transcript": text}, callbacks=callbacks)
    print("[thread] final_result", final_result)
    sendFn(final_result)
    print("[thread] final_result sent", sendFn.__name__)


def transcript_callback(text):
    global ai_note_set
    global state_store
    global diffdiag_prompt
    print("[main] transcript callback. patient_mode:{}, patient_recording:{}".
          format(state_store["patient_mode"],
                 state_store["patient_recording"]))
    if state_store["patient_mode"]:
        send_patient_transcript(text)
    else:
        state_store["transcript"] += text + "\n"
        send_transcript(state_store["transcript"])
        with ThreadPoolExecutor(4) as e:
            e.submit(run_on_transcript, state_store["transcript"], send_cds_qa,
                     questions_prompt)
            e.submit(run_on_transcript, state_store["transcript"],
                     send_cds_ddx, diffdiag_prompt)