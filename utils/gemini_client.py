import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

MODEL = "gemini-3.5-flash"


def ask_gemini(system_prompt, user_prompt):

    response = client.models.generate_content(

        model=MODEL,

        contents=[
            {
                "role": "user",
                "parts": [
                    {
                        "text":
f"""
SYSTEM

{system_prompt}

------------------------------------------------

USER

{user_prompt}
"""
                    }
                ]
            }
        ],
    )

    return response.text.strip()