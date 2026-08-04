import json

from utils.gemini_client import ask_gemini


def analyze_risks():

    with open("output/qualification.json") as f:
        qualification = json.load(f)

    with open("output/strategy.json") as f:
        strategy = json.load(f)

    system_prompt = """
You are an Enterprise Sales Director.

Analyze the opportunity.

Identify:

- technical risks
- commercial risks
- stakeholder risks
- timeline risks
- procurement risks

Assign each a severity.

Return JSON only.
"""

    user_prompt = f"""
Qualification

{json.dumps(qualification, indent=2)}

Strategy

{json.dumps(strategy, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/risk_analysis.json", "w") as f:
        f.write(response)

    print("Risk analysis completed!")