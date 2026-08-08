import streamlit as st


def show_metrics(
    qualification,
    research,
    stakeholders,
):

    score = qualification.get(
        "qualification_score",
        0,
    )

    priority = qualification.get(
        "priority",
        "Medium",
    )

    industry = research.get(
        "industry",
        "Unknown",
    )

    champion = (
        stakeholders.get("champion", {})
        .get("role", "Not Identified")
    )

    economic_buyer = (
        stakeholders.get("economic_buyer", {})
        .get("role", "Not Identified")
    )

    st.subheader("📊 Opportunity Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Qualification Score",
        f"{score}/100",
    )

    c2.metric(
        "Priority",
        priority,
    )

    c3.metric(
        "Industry",
        industry,
    )

    c4, c5 = st.columns(2)

    c4.metric(
        "Champion",
        champion,
    )

    c5.metric(
        "Economic Buyer",
        economic_buyer,
    )

    st.progress(
        min(score / 100, 1.0)
    )