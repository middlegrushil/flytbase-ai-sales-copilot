import streamlit as st


def show_metrics(qualification, research):

    score = qualification.get("qualification_score", 0)

    if score >= 80:
        opportunity = "🟢 HIGH"
    elif score >= 60:
        opportunity = "🟡 MEDIUM"
    else:
        opportunity = "🔴 LOW"

    champion = qualification.get("champion", "Unknown")
    buyer = qualification.get("economic_buyer", "Unknown")
    industry = research.get("industry", "Unknown")

    st.subheader("📊 Opportunity Dashboard")

    c1, c2, c3 = st.columns(3)

    c1.metric(
        "Qualification Score",
        f"{score}/100"
    )

    c2.metric(
        "Opportunity",
        opportunity
    )

    c3.metric(
        "Industry",
        industry
    )

    c1, c2 = st.columns(2)

    c1.metric(
        "Champion",
        champion
    )

    c2.metric(
        "Economic Buyer",
        buyer
    )

    st.progress(score / 100)