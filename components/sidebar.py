import streamlit as st


def show_sidebar():
    """
    Displays the application sidebar.
    """

    with st.sidebar:

        st.title("🚁 FlytBase")

        st.caption("AI Sales Copilot")

        st.divider()

        st.subheader("Workflow")

        workflow = [
            "Lead Qualification",
            "Company Research",
            "Sales Strategy",
            "Solution Recommendation",
            "Meeting Preparation",
            "Follow-up Email",
            "Discovery Questions",
            "Objection Handling",
            "Risk Analysis",
            "Stakeholder Mapping",
            "CRM Summary",
            "Next Best Action",
            "Sales Brief"
        ]

        for step in workflow:
            st.success(f"✓ {step}")

        st.divider()

        st.subheader("Platform")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("LLM", "Gemini")

        with col2:
            st.metric("Search", "Tavily")

        st.metric(
            "AI Agents",
            "12"
        )

        st.metric(
            "Status",
            "Ready"
        )

        st.divider()

        st.info(
            """
### About

This AI Sales Copilot automates the enterprise
sales workflow by:

- Qualifying inbound leads
- Researching companies
- Building sales strategies
- Recommending FlytBase solutions
- Preparing meetings
- Drafting follow-up emails
- Summarizing CRM notes
- Generating executive sales briefs
"""
        )

        st.divider()

        st.caption("FlytBase AI Sales Copilot v1.0")