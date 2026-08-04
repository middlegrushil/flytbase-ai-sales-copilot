import streamlit as st


def show_dashboard(
    qualification,
    research,
    recommendation,
    next_action
):
    """
    Executive dashboard shown after analysis.
    """

    st.header("📊 Executive Dashboard")

    col1, col2 = st.columns(2)

    # ==========================================
    # Left Column
    # ==========================================

    with col1:

        st.subheader("🏢 Company")

        st.info(
            research.get(
                "company_overview",
                "No company overview available."
            )
        )

        st.subheader("🎯 Sales Strategy")

        strategy = recommendation.get(
            "strategy",
            ""
        )

        if strategy:

            st.markdown(strategy)

        else:

            st.markdown(
                recommendation.get(
                    "recommendation",
                    "No recommendation generated."
                )
            )

        st.subheader("💰 Business Value")

        st.write(

            recommendation.get(

                "business_value",

                "Business value not available."

            )

        )

    # ==========================================
    # Right Column
    # ==========================================

    with col2:

        st.subheader("📈 Lead Qualification")

        score = qualification.get(

            "qualification_score",

            0

        )

        st.metric(

            "Qualification Score",

            f"{score}/100"

        )

        st.progress(score / 100 if score else 0)

        st.metric(

            "Industry",

            research.get(

                "industry",

                "Unknown"

            )

        )

        st.metric(

            "Champion",

            qualification.get(

                "champion",

                "Unknown"

            )

        )

        st.metric(

            "Economic Buyer",

            qualification.get(

                "economic_buyer",

                "Unknown"

            )

        )

        st.subheader("➡️ Next Best Action")

        if isinstance(next_action, dict):

            st.success(

                next_action.get(

                    "next_action",

                    "No recommendation."

                )

            )

        else:

            st.success(next_action)

        st.subheader("🚦Opportunity Status")

        if score >= 80:

            st.success("🟢 High Priority Opportunity")

        elif score >= 60:

            st.warning("🟡 Medium Priority Opportunity")

        else:

            st.error("🔴 Low Priority Opportunity")