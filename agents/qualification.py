import json
from utils.gemini_client import ask_gemini

def qualify_lead():

    with open("input/lead.json", "r") as f:
        lead = json.load(f)

    system_prompt = """
You are an Enterprise Solutions Engineer at FlytBase.

Your task is to qualify inbound enterprise leads using the MEDDIC framework while also evaluating the overall business opportunity.

IMPORTANT:
Do NOT assign extremely low scores simply because some MEDDIC information is missing.

The qualification score should represent the overall sales opportunity, not just the completeness of information.

When calculating the score, consider:

- Industry fit for FlytBase
- Company size and enterprise potential
- Relevance of the use case
- Seniority of the contact
- Likelihood of adopting autonomous drone solutions
- MEDDIC completeness

Scoring Guidelines:

90–100:
Excellent enterprise opportunity with strong fit and clear buying signals.

75–89:
High-potential enterprise lead. Some discovery is still required.

60–74:
Good opportunity but several qualification questions remain unanswered.

40–59:
Possible opportunity that requires significant discovery.

0–39:
Poor fit or insufficient information.

Missing information should reduce the score moderately, but should NEVER reduce an otherwise excellent enterprise lead below 60.

Return ONLY valid JSON using exactly this format:

{
  "qualification_score": 0,
  "metrics": "",
  "economic_buyer": "",
  "decision_criteria": "",
  "decision_process": "",
  "identify_pain": "",
  "champion": "",
  "missing_information": [],
  "reasoning": ""
}
"""

    response = ask_gemini(
        system_prompt,
        json.dumps(lead, indent=2)
    )

    with open("output/qualification.json", "w") as f:
        f.write(response)

    print("Lead qualified successfully!")

    return response