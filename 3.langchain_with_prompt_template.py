from langchain_openai import ChatOpenAI
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts import SystemMessagePromptTemplate
from langchain.prompts import ChatPromptTemplate
import os

# Set up API with error handling
os.environ["OPENAI_API_KEY"] = ""


sys_msg = "You are {subject} teacher"
human_msg = "Tell me about the {concept}"

prompt_template = ChatPromptTemplate.from_messages([("system",sys_msg),("human",human_msg)])

prompt = prompt_template.format_messages(subject="Chemistry", concept="Periodic Table")

