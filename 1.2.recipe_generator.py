from openai import OpenAI

client = OpenAI(api_key="")

ingredients = []
#create somehting that can accept ingrediants and return a recipe

while True:
    ingredient = input("Enter an ingredient. Type done once complete:")
    if ingredient.lower() == "done":
        break

    ingredients.append(ingredient)

    
#create a function that uses the model and bring in the ingrediants

def generate_recipe(ingredients):

    messages = []

    for ingredient in ingredients:
        messages.append({"role": "user", "content": ingredient})

    messages.extend([
        {"role": "system", "content": "direct, point"},
        {"role": "assistant", "content": "You are a high-end chef. Generate a recipie based on  the given ingrediants"}
    ]
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        max_tokens=300,
        temperature=0.9
    )

#return the recipie

    return response.choices[0].message.content

print(generate_recipe(ingredients))
