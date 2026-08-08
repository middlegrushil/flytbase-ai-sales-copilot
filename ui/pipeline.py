import os
import time

import streamlit as st

from agents.firecrawl_research import firecrawl_research
from agents.case_study_matcher import match_case_study
from agents.qualification import qualify_lead
from agents.research import company_research
from agents.strategy import create_strategy
from agents.recommendation import recommend_solution
from agents.meeting_prep import generate_meeting_prep
from agents.email_generator import generate_email
from agents.discovery_questions import generate_discovery_questions
from agents.objection_handler import handle_objections
from agents.risk_analysis import analyze_risks
from agents.stakeholder import identify_stakeholders
from agents.partner_recommender import recommend_partner
from agents.crm_summary import generate_crm_summary
from agents.next_action import recommend_next_action
from agents.report import generate_report


PIPELINE = [
    (
        "Building FlytBase Knowledge Base",
        firecrawl_research,
        ["output/flytbase_context.json"],
    ),
    (
        "Matching Similar Customer Case Study",
        match_case_study,
        ["output/case_study.json"],
    ),
    (
        "Qualifying Enterprise Lead",
        qualify_lead,
        ["output/qualification.json"],
    ),
    (
        "Researching Company",
        company_research,
        ["output/research.json"],
    ),
    (
        "Creating Sales Strategy",
        create_strategy,
        ["output/strategy.json"],
    ),
    (
        "Generating Solution Recommendation",
        recommend_solution,
        ["output/recommendation.json"],
    ),
    (
        "Preparing Meeting",
        generate_meeting_prep,
        ["output/meeting_prep.md"],
    ),
    (
        "Generating Follow-up Email",
        generate_email,
        ["output/email.md"],
    ),
    (
        "Generating Discovery Questions",
        generate_discovery_questions,
        ["output/discovery_questions.md"],
    ),
    (
        "Handling Customer Objections",
        handle_objections,
        ["output/objections.json"],
    ),
    (
        "Performing Risk Analysis",
        analyze_risks,
        ["output/risk_analysis.json"],
    ),
    (
        "Identifying Stakeholders",
        identify_stakeholders,
        ["output/stakeholders.json"],
    ),
    (
        "Recommending Partner",
        recommend_partner,
        ["output/partner_recommendation.md"],
    ),
    (
        "Generating CRM Summary",
        generate_crm_summary,
        ["output/crm_summary.md"],
    ),
    (
        "Determining Next Action",
        recommend_next_action,
        ["output/next_action.json"],
    ),
    (
        "Generating Executive Report",
        generate_report,
        ["output/sales_brief.md"],
    ),
]


def output_exists(paths):
    if not paths:
        return False

    return all(
        os.path.exists(path)
        and os.path.getsize(path) > 0
        for path in paths
    )


def run_pipeline():

    os.makedirs("output", exist_ok=True)

    progress = st.progress(0)
    status = st.empty()

    total = len(PIPELINE)

    completed = 0

    for title, func, output_files in PIPELINE:

        completed += 1

        # ==================================================
        # CACHE CHECK
        # ==================================================

        if output_exists(output_files):

            status.info(
                f"♻️ Using existing result — {title}"
            )

            progress.progress(
                completed / total
            )

            continue

        # ==================================================
        # RUN AGENT
        # ==================================================

        status.info(
            f"🚀 {title}"
        )

        try:

            func()

        except Exception as e:

            status.error(
                f"❌ {title}"
            )

            st.exception(e)

            raise

        progress.progress(
            completed / total
        )

        # ==================================================
        # GEMINI FREE-TIER RATE LIMIT PROTECTION
        # ==================================================

        if completed < total:

            status.info(
                f"⏳ Preparing next AI agent..."
            )

            time.sleep(15)

    status.success(
        "✅ Enterprise opportunity successfully analyzed."
    )