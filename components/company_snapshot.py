import streamlit as st


def show_company_snapshot(
    research,
    recommendation,
    case_study,
    qualification,
    stakeholders=None,
):
    """
    Company Intelligence Panel
    """

    if stakeholders is None:
        stakeholders = {}

    score = qualification.get("qualification_score", 0)

    left, right = st.columns([2.3, 1])

    # =====================================================

    with left:

        st.header("🏢 Company Intelligence")

        st.caption(
            "AI-generated business intelligence for this enterprise lead."
        )

        st.info(
            research.get(
                "company_overview",
                "No company overview available."
            )
        )

        st.markdown("---")

        st.subheader("🚁 Recommended FlytBase Solution")

        if isinstance(recommendation, dict):

            solution = recommendation.get(
                "recommended_solution",
                {}
            )

            st.success(
                solution.get(
                    "product",
                    "No recommendation generated."
                )
            )

            st.metric(
                "Overall Fit",
                f"{solution.get('overall_fit_score',0)}/100"
            )

            st.markdown("### Business Value")

            for item in recommendation.get(
                "business_value",
                [],
            ):

                st.markdown(
                    f"✅ **{item.get('benefit','')}**"
                )

                st.caption(
                    item.get(
                        "expected_impact",
                        ""
                    )
                )

        else:

            st.markdown(recommendation)

        st.markdown("---")

        st.subheader("📚 Supporting Customer Success Story")

        if isinstance(case_study, dict):

            st.success(
                case_study.get(
                    "matched_customer",
                    "No customer matched."
                )
            )

            st.metric(
                "Similarity",
                f"{case_study.get('similarity_score',0)}%"
            )

            st.write(
                case_study.get(
                    "why_relevant",
                    ""
                )
            )

        else:

            st.markdown(case_study)

    # =====================================================

    with right:

        st.subheader("📈 Opportunity Assessment")

        st.metric(
            "Industry",
            research.get(
                "industry",
                "Unknown",
            ),
        )

        st.metric(
            "Champion",
            stakeholders.get(
                "champion",
                {},
            ).get(
                "role",
                "Unknown",
            ),
        )

        st.metric(
            "Economic Buyer",
            stakeholders.get(
                "economic_buyer",
                {},
            ).get(
                "role",
                "Unknown",
            ),
        )

        st.markdown("---")

        st.subheader("🎯 AI Confidence")

        confidence = qualification.get(
            "confidence",
            "Medium",
        )

        if confidence == "High":

            st.success("High Confidence")
            st.progress(0.9)

        elif confidence == "Medium":

            st.warning("Medium Confidence")
            st.progress(0.7)

        else:

            st.error("Low Confidence")
            st.progress(0.45)

        st.markdown("---")

        st.subheader("💼 Expected Business Outcomes")

        values = recommendation.get(
            "business_value",
            [],
        )

        if values:

            for item in values:

                st.markdown(
                    f"✅ {item.get('benefit','')}"
                )

        else:

            st.markdown(
                """
✅ Reduced inspection costs

✅ Faster inspections

✅ Improved worker safety

✅ Higher operational efficiency
"""
            )