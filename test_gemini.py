from utils.gemini_client import ask_gemini

system_prompt = "You are a helpful assistant."

user_prompt = "Reply with exactly: Gemini API connection successful."

response = ask_gemini(system_prompt, user_prompt)

print(response)