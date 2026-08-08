
import streamlit as st


def show_sidebar():

    with st.sidebar:

        st.markdown(
            """
            <h2 style="margin-bottom:0px;">
            🚁 FlytBase
            </h2>

            <p style="
            color:#9FB3C8;
            margin-top:0px;
            font-size:14px;
            ">
            Enterprise Sales Intelligence Platform
            </p>
            """,
            unsafe_allow_html=True,
        )

        st.divider()

        # =====================================================

        st.subheader("Platform")

        c1, c2 = st.columns(2)

        with c1:
            st.metric("Status", "🟢")

        with c2:
            st.metric("Version", "v2")

        st.metric(
            "Workflow",
            "Ready"
        )

        st.metric(
            "LLM",
            "Gemini 2.5"
        )

        st.metric(
            "Knowledge Base",
            "Live"
        )

        st.divider()

        # =====================================================

        st.subheader("Workflow")

        workflow = [

            "Company Intelligence",

            "Opportunity Qualification",

            "Solution Engineering",

            "Sales Strategy",

            "Customer Engagement",

            "Executive Brief",

        ]

        for step in workflow:

            st.markdown(f"✅ {step}")

        st.divider()

        # =====================================================

        st.subheader("AI Pipeline")

        st.info(
            """
1. Research Company

↓

2. Qualify Opportunity

↓

3. Recommend Solution

↓

4. Match Case Study

↓

5. Build Sales Strategy

↓

6. Generate Sales Assets
"""
        )

        st.divider()

        # =====================================================

        st.subheader("Business Value")

        st.success("98% Less Research Time")

        st.success("Evidence-Based Decisions")

        st.success("Explainable AI Workflow")

        st.success("Executive Ready Outputs")

        st.divider()

        st.caption(
            "Built for FlytBase Solutions Engineers"
        )