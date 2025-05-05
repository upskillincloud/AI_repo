from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers.list import ListOutputParser
from langchain.output_parsers import CommaSeparatedListOutputParser
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

Prompt = PromptTemplate(
    template="List 3 {things}",  # Shorter prompt
    input_variables=["things"]
)

response = llm.invoke(Prompt.format(things="Countries that play cricket in a world cup"))
print(response.content)  # Just print the content part

output_parser = CommaSeparatedListOutputParser()
format_instructions = output_parser.get_format_instructions()

Prompt = PromptTemplate(
    template="List 3 {things}.\n{format_instruction}",  # Shorter prompt
    input_variables=["things"],
    partial_variables={"format_instruction": format_instructions}
)

final_prompt = Prompt.format(things="Countries that play cricket in a world cup")
output = llm.invoke(final_prompt)
output_text = output.content 
print(output.content.strip())

print(f"Raw output text: {output_text}")

print(f"\nOutput type: {type(output)}")
print(f"Output content type: {type(output_text)}")

things = output_parser.parse(output_text)

print(f"\nParsed list: {things}")
print(f"Parsed list type: {type(things)}")

# Access individual items
if len(things) >= 3:
    print(f"\nFirst country: {things[0]}")
    print(f"Second country: {things[1]}")
    print(f"Third country: {things[2]}")
