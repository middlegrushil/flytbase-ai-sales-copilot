import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

response = client.chat.completions.create(
    model="openrouter/auto",
    messages=[
        {"role": "user", "content": "Say hello in one sentence."}
    ],
    max_tokens=20,
)

print(response.choices[0].message.content)