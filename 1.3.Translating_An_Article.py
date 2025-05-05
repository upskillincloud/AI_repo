from openai import OpenAI

client = OpenAI(api_key="")

# article
#article = "https://www.bbc.com/news/world-asia-67012345"

# below line is in japanese
article = "今日は調子はどうですか？気分はいかがですか？"

#prompt
prompt = f"Translate the following article into English:{article}"
#function that can transalte the article

def article_translator(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "assistant", "content": "You are a professional translator. You translate news articles into english."},
            {"role": "system", "content": "direct english translator"},
        ],
        temperature=0.1
    )
    return response.choices[0].message.content

# print the translated article
print(article_translator(prompt))
