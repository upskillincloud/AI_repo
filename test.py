from langchain import OpenAI
import os
os.setenv("OPENAI_API_KEY") = ""

llm = OpenAI()
text = "What would be a good company name for a company that makes toy for kids"

print(llm.invoke(text))
