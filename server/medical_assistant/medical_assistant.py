from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferWindowMemory
from langchain.agents import Tool, AgentExecutor, LLMSingleActionAgent

from langchain.tools import DuckDuckGoSearchRun 
from typing import List

from assistant_templates import template_without_memory #, template_with_memory
from assistant_utils import CustomPromptTemplate, CustomOutputParser

from dotenv import load_dotenv
load_dotenv()


# Define which tools the agent can use to answer user queries
search = DuckDuckGoSearchRun()

def duck_wrapper_drugs(input_text):
    search_results = search.run(f"site:drugs.com {input_text}")
    return search_results

def duck_wrapper_webmd(input_text):
    search_results = search.run(f"site:webmd.com {input_text}")
    return search_results

tools = [
    Tool(
        name = "Search drugs.com",
        func=duck_wrapper_drugs,
        description="useful for when you need to answer medication questions"
    ),

    Tool(
        name = "Search webmd.com",
        func=duck_wrapper_webmd,
        description="useful for when you need to answer medication questions"
    )
]
    


prompt_without_memory = CustomPromptTemplate(
    template=template_without_memory,
    tools=tools,
    # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
    # This includes the `intermediate_steps` variable because that is needed
    input_variables=["input", "intermediate_steps"]
)

# prompt_with_history = CustomPromptTemplate(
#     template=template_with_memory,
#     tools=tools,
#     # This omits the `agent_scratchpad`, `tools`, and `tool_names` variables because those are generated dynamically
#     # This includes the `intermediate_steps` variable because that is needed
#     input_variables=["input", "intermediate_steps", "history"]
# )



output_parser = CustomOutputParser()


llm = OpenAI(temperature=0)

# LLM chain consisting of the LLM and a prompt
llm_chain = LLMChain(llm=llm, prompt=prompt_without_memory)
# llm_chain = LLMChain(llm=llm, prompt=prompt_with_history)


memory=ConversationBufferWindowMemory(k=2)

tool_names = [tool.name for tool in tools]

agent = LLMSingleActionAgent(
    llm_chain=llm_chain, 
    output_parser=output_parser,
    stop=["\nObservation:"], 
    allowed_tools=tool_names
)



agent_executor = AgentExecutor.from_agent_and_tools(agent=agent, 
                                                    tools=tools, 
                                                    verbose=True
                                                    #,memory=memory
                                                    )