from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers.list import ListOutputParser
from langchain_core.output_parsers import JsonOutputParser
import os
import json

# Set up API with error handling
os.environ["OPENAI_API_KEY"] = ""


# Create the LangChain OpenAI LLM object with economic settings
llm = ChatOpenAI(  # Changed from OpenAI to ChatOpenAI
    model="gpt-4o-mini",  # Most economical completion model
    temperature=0,  # More deterministic (potentially shorter) responses
    max_tokens=300,  # Limit response length
    request_timeout=10  # Timeout quickly if there's an issue
)

prompt = PromptTemplate(
    template="List 3 countries in the {continent} and thier capitals",  # Shorter prompt
    input_variables=["continent"]
)
response = llm.invoke(prompt.format(continent="asia"))
#print(response.content)  # Just print the content part


output_parser = JsonOutputParser()
format_instructions = output_parser.get_format_instructions()
#print(f"Format instructions: {format_instructions}")
prompt = PromptTemplate(
    template="List 3 countries in the {continent} and thier capitals.\n{format_instruction}",  # Shorter prompt
    input_variables=["continent"],
    partial_variables={"format_instruction": format_instructions}
)
final_prompt = prompt.format(continent="North America")
output = llm.invoke(final_prompt)
output_text = output.content
print(output.content)
#print(f"Raw output text: {output_text}")
#print(f"\nOutput type: {type(output)}")
#print(f"Output content type: {type(output_text)}")
# Parse the output
try:
    parsed_output = output_parser.parse(output_text)
    print(f"\nParsed output: {parsed_output}") 
    # Access individual items
    if isinstance(parsed_output, dict):
        for key, value in parsed_output.items():
            print(f"{key}: {value}")
    else:
        print("Parsed output is not a dictionary.")
except json.JSONDecodeError as e:
    print(f"Failed to parse JSON: {e}")
# Note: The above code assumes that the output from the LLM is in a valid JSON format.
# If the output is not in a valid JSON format, the parsing will fail.
# The error handling for JSON parsing is included to catch any issues with the output format.
# The code is designed to work with the LangChain library and OpenAI's API.
# The output parser is set to parse JSON, and the prompt is designed to request a JSON response.
# The code includes error handling for JSON parsing and prints the parsed output.
# The code is designed to be run in an environment where the LangChain library and OpenAI's API are available.
# The code is a demonstration of how to use the LangChain library to interact with OpenAI's API


countries = output_parser.parse(output_text)
type(countries)
print(f"Parsed list type: {type(countries)}")
json_output =  json.dumps(countries)
print("======================")
print(json_output)
print("======================")

