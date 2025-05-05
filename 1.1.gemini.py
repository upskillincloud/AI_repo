from langchain_google_genai import GoogleGenerativeAI
import os

os.environ["GOOGLE_API_KEY"]=""

llm = GoogleGenerativeAI(model="gemini-pro")

text = "What would be a good company name for a company that makes toys for kids?"

print(llm.invoke(text))