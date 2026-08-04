import json

from utils.gemini_client import ask_gemini


def generate_discovery_questions():

    with open("output/research.json") as f:
        research = json.load(f)

    with open("output/recommendation.json") as f:
        recommendation = json.load(f)

    system_prompt = """
Generate 10 enterprise discovery questions.

Focus on:

- operations

- inspection workflow

- automation

- safety

- budget

- implementation

Return Markdown.
"""

    user_prompt = f"""
Research

{json.dumps(research, indent=2)}

Recommendation

{json.dumps(recommendation, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/discovery_questions.md", "w") as f:
        f.write(response)

    print("Discovery questions generated!")