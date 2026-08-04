import json
import os

from utils.gemini import ask_gemini


def recommend_solution():
    """
    Generates a FlytBase-specific solution recommendation by combining:
    - Lead information
    - Tavily company research
    - FlytBase knowledge (Firecrawl)
    - Similar case study
    """

    # -------------------------------
    # Load Lead
    # -------------------------------

    with open("input/lead.json") as f:
        lead = json.load(f)

    # -------------------------------
    # Load Company Research
    # -------------------------------

    research = {}

    if os.path.exists("output/research.json"):
        with open("output/research.json") as f:
            research = json.load(f)

    # -------------------------------
    # Load FlytBase Knowledge
    # -------------------------------

    flytbase = {}

    if os.path.exists("output/flytbase_context.json"):
        with open("output/flytbase_context.json") as f:
            flytbase = json.load(f)

    # -------------------------------
    # Load Case Study
    # -------------------------------

    case_study = {}

    if os.path.exists("output/case_study.json"):
        with open("output/case_study.json") as f:
            case_study = json.load(f)

    # -------------------------------
    # Extract Knowledge
    # -------------------------------

    solution_info = flytbase.get("solutions", {}).get("markdown", "")

    product_info = flytbase.get("products", {}).get("markdown", "")

    case_info = case_study.get("case_study", "")

    company = lead.get("company", "")

    industry = lead.get("industry", "")

    use_case = lead.get("use_case", "")

    company_research = research.get("research", "")

    # -------------------------------
    # Build Prompt
    # -------------------------------

    prompt = f"""
You are a Senior Solutions Engineer at FlytBase.

Your job is to recommend the BEST FlytBase solution for an inbound enterprise customer.

=========================
LEAD
=========================

Company:
{company}

Industry:
{industry}

Use Case:
{use_case}

=========================
COMPANY RESEARCH
=========================

{company_research}

=========================
FLYTBASE SOLUTIONS
=========================

{solution_info}

=========================
FLYTBASE PRODUCTS
=========================

{product_info}

=========================
SIMILAR CASE STUDY
=========================

{case_info}

=========================

Prepare a recommendation including:

1. Customer pain points

2. Recommended FlytBase products

3. Why these products fit

4. Expected ROI

5. Implementation roadmap

6. Risks

7. Mention the similar FlytBase customer success story naturally.

Return clean markdown.
"""

    recommendation = ask_gemini(prompt)

    os.makedirs("output", exist_ok=True)

    with open("output/recommendation.json", "w") as f:
        json.dump(
            {
                "recommendation": recommendation
            },
            f,
            indent=4,
        )

    print("✅ Recommendation generated.")