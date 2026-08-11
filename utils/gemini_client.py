import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise RuntimeError("GEMINI_API_KEY is not configured.")

client = genai.Client(api_key=API_KEY)

MODEL = "gemini-3.5-flash"


def ask_gemini(system_prompt, user_prompt):

    try:

        response = client.models.generate_content(
            model=MODEL,
            contents=[
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": (
                                f"SYSTEM INSTRUCTIONS:\n"
                                f"{system_prompt}\n\n"
                                f"USER REQUEST:\n"
                                f"{user_prompt}"
                            )
                        }
                    ],
                }
            ],
        )

        return response.text

    except Exception as e:

        raise RuntimeError(e)