import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)

MODEL = "google/gemini-2.5-flash-lite"


def ask_gemini(prompt: str) -> str:
    """
    Single LLM wrapper used by every AI agent.
    (Function name kept as ask_gemini so no agent code changes are needed.)
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            temperature=0.3,
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("\n========== LLM ERROR ==========")
        print(e)
        print("===============================\n")

        raise RuntimeError(f"LLM Error: {e}")