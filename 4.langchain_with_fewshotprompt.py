from langchain.prompts import ChatPromptTemplate
from langchain.prompts import FewShotChatMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os

# Set up API with error handling
os.environ["OPENAI_API_KEY"] = ""

# Define the examples for FewShotPromptTemplate

examples = [
    { "input": "India", "output": "aidnI" },
    { "input": "USA", "output": "ASU" },
    { "input": "China", "output": "anihC" },
]

example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{input}"),
    ("ai", "{output}"),
])

few_shot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

print(few_shot_prompt.format())

Prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a linguistic specialist"),
        few_shot_prompt,
        ("human", "{input}"),
    ]
)

prompt = Prompt_template.format_messages(input="Brazil")

model = ChatOpenAI(
        model="gpt-4o-mini",  # Specify a potentially less expensive model
        temperature=0,
        max_tokens=150
    )

# Try to get a response
response = model.invoke(prompt)
print(response.content)
