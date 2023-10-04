from langchain.memory import ConversationBufferMemory


project_name = "PremierHealthAI"
memory = ConversationBufferMemory(ai_prefix=project_name, human_prefix="Patient")
memory.chat_memory.add_ai_message(
    f"Hello, I'm {project_name}, your medical knowledge assistant. How can I assist you today with your prescriptions?"
)

memory.chat_memory.add_user_message

state_store = {
    "transcript": "",
    "pharmacist_summary": "",
    "patient_instruction_memory": memory,
    "patient_mode": False,
    "patient_recording": False
}
