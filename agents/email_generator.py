import json

from utils.gemini_client import ask_gemini


def generate_email():

    with open("input/lead.json") as f:
        lead = json.load(f)

    with open("output/research.json") as f:
        research = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    with open("output/recommendation.json") as f:
        recommendation = json.load(f)

    system_prompt = """
You are a Senior Enterprise Account Executive at FlytBase.

Write a professional follow-up email after an introductory discovery call.

The email should:

- Thank the customer
- Summarize their business challenges
- Explain how FlytBase can help
- Mention the recommended solution
- Suggest the next meeting
- Sound natural and professional

Return Markdown only.
"""

    user_prompt = f"""
Lead

{json.dumps(lead, indent=2)}

Research

{json.dumps(research, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}

Recommendation

{json.dumps(recommendation, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/followup_email.md", "w") as f:
        f.write(response)

    print("Follow-up email generated!")