
[root@test-inst ai]# cat langchain_example_final.py
from langchain_openai import ChatOpenAI  # Changed from OpenAI to ChatOpenAI
from langchain.prompts import PromptTemplate
import os

# Set the API key
os.environ["OPENAI_API_KEY"] = ""

# Create the LangChain OpenAI LLM object with economic settings
llm = ChatOpenAI(  # Changed from OpenAI to ChatOpenAI
    model="gpt-4o-mini",  # Most economical completion model
    temperature=0,  # More deterministic (potentially shorter) responses
    max_tokens=30,  # Limit response length
    request_timeout=10  # Timeout quickly if there's an issue
)

# Create a prompt template (keep it short)
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Suggest one name for {topic} company:"  # Shorter prompt
)

# Create a chain using the modern pipe syntax
chain = prompt | llm

try:
    # Run the chain with invoke
    result = chain.invoke({"topic": "toy"})  # Shorter input
    print(result)
except Exception as e:
    print(f"Error: {e}")
    print("Fallback: ToyJoy")
[root@test-inst ai]#

[root@test-inst ai]# python3.9 langchain_example3.py

sudo dnf module install python39
 pip3 install openai
 python3.9 -m pip install langchain langchain-openai
