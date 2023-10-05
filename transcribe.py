from app import send_transcript, send_patient_transcript, send_cds_ddx, send_cds_qa
from state import state_store
from model import diffdiag_and_questions_writer, diffdiag_prompt, questions_prompt
from socketcallback import SocketIOCallback
from concurrent.futures import ThreadPoolExecutor