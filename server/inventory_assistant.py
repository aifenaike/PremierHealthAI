## Path to medical_assiatant functinalities
import sys
sys.path.append('./database')
import pandas as pd


from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_csv_agent
from langchain.llms import OpenAI


inventory_agent = create_csv_agent(OpenAI(temperature=0), 
                         r"C:/Users/HP/Desktop/PremierHealthAI/database/PremierHealthAI_DB.csv", 
                         verbose=True)

# print(agent.run("How many dosage?"))