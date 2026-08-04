import time
import streamlit as st

from agents.qualification import qualify_lead
from agents.firecrawl_research import firecrawl_research
from agents.case_study_matcher import match_case_study
from agents.research import research_company
from agents.strategy import create_strategy
from agents.recommendation import recommend_solution
from agents.partner_recommender import recommend_partner
from agents.meeting_prep import generate_meeting_prep
from agents.email_generator import generate_email
from agents.discovery_questions import generate_discovery_questions
from agents.objection_handler import generate_objections
from agents.risk_analysis import analyze_risks
from agents.stakeholder import identify_stakeholders
from agents.crm_summary import generate_crm_summary
from agents.next_action import generate_next_action
from agents.report import generate_report


def run_pipeline():

    st.subheader("🤖 AI Workflow")

    progress = st.progress(0)

    status = st.empty()

    pipeline = [

        ("Firecrawl Knowledge Base", firecrawl_research),

        ("Lead Qualification", qualify_lead),

        ("Company Research", research_company),

        ("Case Study Matching", match_case_study),

        ("Sales Strategy", create_strategy),

        ("Solution Recommendation", recommend_solution),

        ("Partner Recommendation", recommend_partner),

        ("Meeting Preparation", generate_meeting_prep),

        ("Follow-up Email", generate_email),

        ("Discovery Questions", generate_discovery_questions),

        ("Objection Handling", generate_objections),

        ("Risk Analysis", analyze_risks),

        ("Stakeholder Mapping", identify_stakeholders),

        ("CRM Summary", generate_crm_summary),

        ("Next Best Action", generate_next_action),

        ("Executive Sales Brief", generate_report)

    ]

    total_steps = len(pipeline)

    for i, (step_name, function) in enumerate(pipeline):

        status.info(f"⚙️ Running **{step_name}**...")

        try:
            function()

        except Exception as e:

            st.error(f"❌ {step_name} failed")

            st.exception(e)

            return

        progress.progress((i + 1) / total_steps)

        time.sleep(0.2)

    status.success("✅ AI Workflow Completed Successfully!")

    st.success("🎉 FlytBase AI Sales Copilot has completed the analysis.")