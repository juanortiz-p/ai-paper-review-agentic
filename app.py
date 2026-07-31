from pathlib import Path

import streamlit as st

from src.workflow import run_pipeline


PROJECT_ROOT = Path(__file__).resolve().parent
FINAL_REPORT_PATH = PROJECT_ROOT / "data" / "output" / "final_report.json"


st.set_page_config(
    page_title="AI Paper Review Agentic",
    page_icon="📚",
    layout="wide",
)


# -------------------------------------------------------------------
# Header
# -------------------------------------------------------------------

st.title("📚 AI Paper Review Agentic")

st.write(
    """
    A multi-agent research assistant that searches, analyzes and reviews
    scientific papers from arXiv.

    The system uses four specialized agents:

    1. **Query Builder Agent** — transforms your research topic into an arXiv query.
    2. **Search Agent** — retrieves recent papers from arXiv.
    3. **Analyst Agent** — analyzes each paper and evaluates its relevance.
    4. **Reviewer Agent** — checks the analyses and corrects unsupported claims.
    5. **Editor Agent** — produces the final research briefing.
    """
)

st.divider()


# -------------------------------------------------------------------
# User input
# -------------------------------------------------------------------

st.header("Start a research")

research_topic = st.text_area(
    "What would you like to investigate?",
    value=(
        "I want to investigate multi-agent AI systems "
        "applied to automated data analytics."
    ),
    height=120,
    placeholder="Describe the topic you want to investigate...",
)

st.caption(
    "The complete pipeline can take around one or two minutes, "
    "depending on the number of papers and API response times."
)


# -------------------------------------------------------------------
# Pipeline execution
# -------------------------------------------------------------------

if st.button(
    "▶ Run research agents",
    type="primary",
    use_container_width=True,
):
    if not research_topic.strip():
        st.warning("Enter a research topic before running the agents.")

    else:
        progress_bar = st.progress(
            0,
            text="Preparing research pipeline...",
        )

        status_box = st.empty()

        def update_progress(percentage: int, message: str) -> None:
            progress_bar.progress(
                percentage,
                text=message,
            )
            status_box.info(message)

        try:
            with st.status(
                "Running agentic research pipeline...",
                expanded=True,
            ) as status:

                report = run_pipeline(
                    research_topic=research_topic,
                    progress_callback=update_progress,
                )

                st.session_state["final_report"] = report

                status.update(
                    label="Research completed successfully",
                    state="complete",
                    expanded=False,
                )

            progress_bar.progress(
                100,
                text="Research completed successfully",
            )

            status_box.success(
                "All agents completed their tasks."
            )

        except Exception as error:
            progress_bar.empty()
            status_box.error(
                "The research pipeline could not be completed."
            )

            with st.expander("Show error details"):
                st.code(str(error))


st.divider()


# -------------------------------------------------------------------
# Load report
# -------------------------------------------------------------------

final_report = st.session_state.get("final_report")

if final_report is None and FINAL_REPORT_PATH.exists():
    import json

    with FINAL_REPORT_PATH.open(
        encoding="utf-8",
    ) as file:
        final_report = json.load(file)


# -------------------------------------------------------------------
# Results
# -------------------------------------------------------------------

st.header("Research results")

if final_report is None:
    st.info(
        "Run the research agents to generate a report."
    )

else:
    report = final_report["report"]
    papers = final_report.get("papers", [])

    # General information
    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Papers found",
        final_report.get("papers_found", 0),
    )

    col2.metric(
        "Papers approved",
        final_report.get("papers_approved", 0),
    )

    approval_rate = (
        final_report.get("papers_approved", 0)
        / final_report.get("papers_found", 1)
    )

    col3.metric(
        "Approval rate",
        f"{approval_rate:.0%}",
    )

    st.subheader("Research topic")
    st.write(final_report["research_topic"])

    with st.expander("View generated arXiv query"):
        st.code(
            final_report["arxiv_query"],
            language=None,
        )

    # Executive summary
    st.subheader("Executive summary")
    st.write(report["executive_summary"])

    # Trends and differences
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Main trends")

        for trend in report.get("main_trends", []):
            st.markdown(f"- {trend}")

    with col2:
        st.subheader("Key differences")

        for difference in report.get(
            "key_differences",
            [],
        ):
            st.markdown(f"- {difference}")

    # Reading order
    st.subheader("Recommended reading order")

    for item in report.get(
        "recommended_reading_order",
        [],
    ):
        with st.container(border=True):
            st.markdown(
                f"### {item['position']}. {item['title']}"
            )
            st.write(item["reason"])

    # Final recommendation
    st.subheader("Final recommendation")
    st.success(report["final_recommendation"])

    # Papers
    st.subheader("Reviewed papers")

    for paper in papers:
        score = paper.get("relevance_score", "N/A")

        with st.expander(
            f"{score}/10 — {paper['title']}"
        ):
            st.write(
                f"**Authors:** {paper.get('authors', 'Unknown')}"
            )

            st.write(
                f"**Published:** {paper.get('published', 'Unknown')}"
            )

            st.write("**Summary**")
            st.write(paper.get("summary", ""))

            st.write("**Main contribution**")
            st.write(
                paper.get("main_contribution", "")
            )

            st.write("**Potential applications**")
            st.write(paper.get("applications", ""))

            st.write("**Limitations**")
            st.write(paper.get("limitations", ""))

            st.write("**Relevance**")
            st.write(
                paper.get("relevance_reason", "")
            )

            st.link_button(
                "Open paper in arXiv",
                paper["url"],
            )

    # Raw output
    with st.expander("View complete JSON output"):
        st.json(final_report, expanded=False)