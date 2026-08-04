import json

from utils.gemini_client import ask_gemini


def generate_discovery_questions():

    with open("output/research.json") as f:
        research = json.load(f)

    with open("output/recommendation.json") as f:
        recommendation = json.load(f)

    system_prompt = """
You are a Senior Enterprise Solutions Engineer at FlytBase.

Generate 10 enterprise discovery questions that will help the sales team better understand the customer's business.

Focus on:

- Current inspection workflow
- Operational challenges
- Drone usage
- Automation maturity
- Safety
- Budget
- Deployment timeline
- Technical requirements
- Success metrics
- Scalability

Return the response in Markdown.
"""

    user_prompt = f"""
Company Research

{json.dumps(research, indent=2)}

====================================================

Recommended Solution

{json.dumps(recommendation, indent=2)}
"""

    response = ask_gemini(system_prompt, user_prompt)

    with open("output/discovery_questions.md", "w") as f:
        f.write(response)

    print("Discovery questions generated!")