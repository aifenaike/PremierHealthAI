from langchain.chat_models import ChatOpenAI
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain.prompts.prompt import PromptTemplate
from langchain.chains import LLMChain, ConversationChain

from state import state_store
from model_templates import diagnosis_report_template, diffdiag_and_questions_template, diffdiag_template, questions_template

from dotenv import load_dotenv

load_dotenv()
import os

key = os.getenv("OPENAI_API_KEY")

# ===========================================================================================
# ===========================================================================================
# ===========================================================================================
gpt3 = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature=0.2,
    streaming=True,
    verbose=True,openai_api_key=key)

gpt4 = ChatOpenAI(model='gpt-4', temperature=0.2, streaming=True, verbose=True,openai_api_key=key)

# ===========================================================================================
# ===========================================================================================
# ===========================================================================================

diagnosis_report_writer_template = PromptTemplate(
    input_variables=["transcript", "pharmacist_hints"],
    template = diagnosis_report_template)

## ===========================================================================================
## ===========================================================================================
## ===========================================================================================

diffdiag_and_questions_writer_template = PromptTemplate(
    input_variables=["transcript"],
    template = diffdiag_and_questions_template)

## ===========================================================================================
## ===========================================================================================
## ===========================================================================================

diffdiag_template_prompt = PromptTemplate(input_variables=["transcript"],
                                       template= diffdiag_template)

## ===========================================================================================
## ===========================================================================================
## ===========================================================================================

questions_template_prompt = PromptTemplate(input_variables=["transcript"],
                                      template=questions_template)


## ===========================================================================================
## ===========================================================================================
## ===========================================================================================

diffdiag_and_questions_writer = LLMChain(llm=gpt3, prompt=diffdiag_and_questions_writer_template, verbose=True)

diffdiag_prompt = LLMChain(llm=gpt3, prompt= diffdiag_template_prompt, verbose=True)

questions_prompt = LLMChain(llm=gpt3, prompt=questions_template_prompt, verbose=True)

diagnosis_report_writer = LLMChain(llm=gpt3,
                                prompt=diagnosis_report_writer_template,
                                verbose=True)

# ===========================================================================================
# ===========================================================================================
# ===========================================================================================

# patient_instructions_template = PromptTemplate(
#     input_variables=["history", "input", "pharmacist_summary"],
#     template=chatbot_template)


# patient_instructor = LLMChain(llm=gpt3,
#                               prompt=patient_instructions_template,
#                               verbose=True)

# ===========================================================================================
# ===========================================================================================
# ===========================================================================================

# inventory_instructions_template = PromptTemplate(
#     input_variables=["history", "input"],
#     template=inventory_chatbot_template)


# inventory_instructor = LLMChain(llm=gpt3,
#                               prompt=inventory_instructions_template,
#                               verbose=True)