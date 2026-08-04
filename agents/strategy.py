import json

from utils.gemini_client import ask_gemini


def create_strategy():

    with open("input/lead.json") as f:
        lead = json.load(f)

    with open("output/qualification.json") as f:
        qualification = json.load(f)

    with open("output/research.json") as f:
        research = json.load(f)

    prompt = f"""
You are an Enterprise Sales Manager at FlytBase.

Below is the lead information.

Lead:
{json.dumps(lead, indent=2)}

Qualification:
{json.dumps(qualification, indent=2)}

Research:
{research}

Your task:

Suggest:

1. Should Sales pursue this lead?
2. What should be discussed during the discovery call?
3. Which FlytBase features solve their pain?
4. Which FlytBase case studies should be shared?
5. Biggest risks in this opportunity.
6. Next best action.

Return ONLY valid JSON.
"""

    response = ask_gemini(
        "You are a sales strategist.",
        prompt
    )

    with open("output/strategy.json", "w") as f:
        f.write(response)

    print("Strategy completed!")

    return response