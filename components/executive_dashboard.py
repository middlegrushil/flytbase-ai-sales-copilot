import streamlit as st


def show_executive_dashboard(
    qualification,
    research,
    recommendation,
    next_action,
):

    score = qualification.get("qualification_score", 0)

    priority = qualification.get(
        "priority",
        "Medium"
    )

    confidence = qualification.get(
        "confidence",
        "Medium"
    )

    company = (
        research.get("company_name")
        or research.get("company")
        or "Unknown Company"
    )

    industry = research.get(
        "industry",
        "Unknown"
    )

    product = (
        recommendation
        .get("recommended_solution", {})
        .get("product", "Not Identified")
    )

    st.header("🚁 Executive Decision Dashboard")

    st.caption(
        "Enterprise AI opportunity assessment"
    )

    st.divider()

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Qualification Score",
        f"{score}/100"
    )

    c2.metric(
        "Priority",
        priority
    )

    c3.metric(
        "Industry",
        industry
    )

    c4.metric(
        "Recommended Solution",
        product
    )

    st.progress(min(score / 100, 1.0))

    st.divider()

    st.subheader("Executive Recommendation")

    if isinstance(next_action, dict):

        st.success(
            next_action.get(
                "next_action",
                "Proceed with Discovery."
            )
        )

    else:

        st.success("Proceed with Discovery.")

    st.info(f"""
### Customer

**{company}**

Industry: **{industry}**

Recommended Solution:

**{product}**

Qualification Score:

**{score}/100**

Priority:

**{priority}**
""")

    st.divider()

    left, right = st.columns([2, 1])

    with left:

        st.subheader("Customer Pain Points")

        pains = recommendation.get(
            "customer_pain_points",
            []
        )

        if pains:

            for pain in pains:

                st.success(
                    pain.get(
                        "pain",
                        ""
                    )
                )

        else:

            st.info("No pain points generated.")

        st.divider()

        st.subheader("Expected Business Value")

        values = recommendation.get(
            "business_value",
            []
        )

        if values:

            for value in values:

                st.markdown(
                    f"✅ **{value.get('benefit','')}**"
                )

                st.caption(
                    value.get(
                        "expected_impact",
                        ""
                    )
                )

        else:

            st.info("No business value generated.")

    with right:

        st.subheader("Opportunity")

        st.metric(
            "Confidence",
            confidence
        )

        st.metric(
            "Priority",
            priority
        )

        st.metric(
            "Qualification",
            f"{score}/100"
        )

        st.divider()

        st.subheader("AI Efficiency")

        st.metric(
            "Manual Research",
            "2 hrs"
        )

        st.metric(
            "AI Runtime",
            "2 mins"
        )

        st.metric(
            "Time Saved",
            "98%"
        )

    st.divider()

    st.subheader("AI Workflow")

    st.markdown("""
1. Company Research

2. Qualification

3. Case Study Matching

4. Solution Recommendation

5. Sales Strategy

6. Meeting Preparation

7. Executive Report
""")