import streamlit as st


def show_metric_cards(
    qualification,
    research
):

    st.header("📌 Executive Summary")

    score = qualification.get(
        "qualification_score",
        0
    )

    industry = research.get(
        "industry",
        "Unknown"
    )

    champion = qualification.get(
        "champion",
        "Unknown"
    )

    buyer = qualification.get(
        "economic_buyer",
        "Unknown"
    )

    c1, c2, c3, c4 = st.columns(4)

    c1.metric(
        "Qualification",
        f"{score}/100"
    )

    c2.metric(
        "Industry",
        industry
    )

    c3.metric(
        "Champion",
        champion
    )

    c4.metric(
        "Economic Buyer",
        buyer
    )