import json

from utils.gemini_client import ask_gemini


def generate_next_action():

    with open("output/qualification.json") as f:
        qualification = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    system_prompt = """
You are a Sales Manager.

Recommend the immediate next sales action.

Return JSON only.

Fields:

priority

owner

action

timeline

reason
"""

    user_prompt = f"""
Qualification

{json.dumps(qualification, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/next_action.json", "w") as f:
        f.write(response)

    print("Next action generated!")