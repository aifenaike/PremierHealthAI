from langchain.memory import ConversationBufferMemory


project_name = "PremierHealthAI"
human_name = "Pharmacist"

memory = ConversationBufferMemory(ai_prefix=project_name, human_prefix=human_name)
memory.chat_memory.add_ai_message(
    f"Hello, I'm {project_name}, your medical knowledge assistant. How can I assist you today with your any medications?"
)

inventory_memory = ConversationBufferMemory(ai_prefix=project_name, human_prefix=human_name)
inventory_memory.chat_memory.add_ai_message(
    f"Hello, I'm {project_name}, your inventory knowledge assistant. How can I assist you today with your Inventory?"
)

memory.chat_memory.add_user_message

state_store = {
    "transcript": "",
    "pharmacist_summary": "",

    "patient_instruction_memory": memory,
    "patient_mode": False,
    "patient_recording": False,

    "inventory_instruction_memory": inventory_memory,
    "inventory_assistant_mode":False,
    "inventory_assistant_recording": False,
}
