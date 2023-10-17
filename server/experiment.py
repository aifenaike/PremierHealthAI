### ---------------------------------------------------------------------- EXPERIMENT NOT CONFIRMED (PC SYSTEM COMPATIBILITY PROBLEM)

# from text_to_speeh_google import synthesize


# def save_to_audio_file(audio_content):
#     with open("experiment.mp3", "wb") as out:
#         # Write the response to the output file.
#         out.write(audio_content)
#         print('Audio content written to file "output.mp3"')

# text = "This is team Premier AI. The teaam includes, James, Sodiq and Alexander. This is enexperiment which happen to be successful"

# audio_exp = synthesize(text)
# save_to_audio_file(audio_exp)



### ---------------------------------------------------------------------- EXPERIMENT 1
from model import diffdiag_prompt, diagnosis_report_writer, questions_prompt, patient_instructor

# transcript = """
# Patient: “I've been taking the Glycomet-GP 1 as you prescribed, doctor, but I'm still feeling quite unwell. My blood pressure readings are all over the place and my sugar levels are high.”
# Doctor: “I see, we may need to adjust your medications. Let's add Jalra-OD and Telmis to your regimen and see how you respond.”
# Doctor's Hint: The patient has uncontrolled diabetes and hypertension despite adherence to the Glycomet-GP 1.
# """

# pharmacist_hints = "Uncontrolled Diabetes and Hypertension"


# ## Tested
# notes = diffdiag_prompt.run(
#         {
#             "transcript": transcript
#         }
#         )

# print(notes)

### ---------------------------------------------------------------------- EXPERIMENT 2


### Tested
# notes = diagnosis_report_writer.run(
#         {
#             "pharmacist_hints": pharmacist_hints,
#             "transcript": transcript
#         })

# print(notes)

### Tested
# notes = questions_prompt.run(
#         {
#             "transcript": transcript
#         }
#         )

# print(notes)

### ---------------------------------------------------------------------- EXPERIMENT 2

# text = "What was my diagnosis?"

# history = ""

# pharmacist_summary = """
# Diagnosis Report:

# Symptom statement: The symptoms mentioned by the patient are a headache, sore throat, and cough

# Diagnosis: Mild respiratory infection

# History of Presenting Illness: The patient has been using panadol but there seems to be no change

# Initial treatment: 
# - Panadol
# Medications (Prescribed):
# [Continue] Panadol
# [Added] Acetaminophen (e.g., Tylenol) or ibuprofen (e.g., Advil, Motrin) | Pain and Fever Relievers:
#    - These over-the-counter (OTC) medications can help reduce fever and alleviate aches and pains associated with respiratory infections.
# [Added] Pseudoephedrine (e.g., Sudafed) or phenylephrine (e.g., Sudafed PE) | Decongestants:
#    - Decongestants can provide temporary relief from nasal congestion, but they should be used cautiously and for a short duration.
# [Added] Loratadine (e.g., Claritin) or cetirizine (e.g., Zyrtec) | Antihistamines:
#    - Antihistamines may help with symptoms like sneezing and runny nose, particularly if allergies contribute to your symptoms.

# Specific Advice for the Patient:
# - Do not give the child sugary drinks, herbal tea, or coffee.
# - Food should be processed and mashed. Maintain regular daily meals: encourage eating more if the child wants to, and eat frequently in small amounts, with meals spaced 3-4 hours apart (6 meals a day). Avoid diluting food. Avoid too many fibrous fruits and vegetables and foods with excessive sugar.
# - Seek medical attention if there are symptoms: continuous watery stools, recurring vomiting, excessive thirst, poor appetite, refusing to eat or breastfeed, no improvement after 2 days of treatment, high fever, blood in stool.
# """
# ## Tested
# notes = patient_instructor.run(
#         {
#             "input": text,
#             "history": history,
#             "pharmacist_summary":pharmacist_summary
#         })

# print(notes)



### ---------------------------------------------------------------------- EXPERIMENT 3

# from utils import recognizer, get_mic_index, microphone
# import speech_recognition as sr
# # from pydub import AudioSegment
# from dotenv import load_dotenv
# import pyaudio

# load_dotenv()


# def process_audio(recognizer, audio):
#     text = recognizer.recognize_whisper_api(audio)
#     print("[whisper] transcript: ", text)


# # List available microphones (optional)
# # for index, name in enumerate(sr.Microphone.list_microphone_names()):
# #     print(f"Microphone {index}: {name}")

# # Use the microphone to capture audio input
# with microphone as source:
#     print("Listening...")
#     audio = recognizer.listen(source)

# process_audio(recognizer, audio)

import sys
sys.path.append('./medical_assistant')

from medical_assistant import medical_assistant
from state import state_store


text = "What are the side effects of panadol?"

ai_response = medical_assistant.agent_executor.run(
    {
        "input": text,
   })

print(f"AI response: {ai_response}")




# from medical_assistant import medical_assistant, assistant_templates



# print(assistant_templates.add_nums(10,20))
# # print(f"w : {medical_assistant.w}")