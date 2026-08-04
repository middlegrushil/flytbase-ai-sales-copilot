import json

from utils.gemini_client import ask_gemini


def generate_objections():

    with open("output/research.json") as f:
        research = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    with open("output/recommendation.json") as f:
        recommendation = json.load(f)

    system_prompt = """
You are a Senior Solutions Engineer at FlytBase.

Predict the customer's most likely objections.

For each objection provide:

- objection
- why they might have it
- recommended response
- confidence

Return valid JSON.

Do not use markdown.
"""

    user_prompt = f"""
Research

{json.dumps(research, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}

Recommendation

{json.dumps(recommendation, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/objections.json", "w") as f:
        f.write(response)

    print("Objection analysis completed!")