import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="HDFC MF FAQ",
    page_icon="📊",
    layout="centered",
)

# ── Lookup table ──────────────────────────────────────────────────────────────
# Source: Groww scheme pages (direct-plan, growth option).
# Expense ratios and AUM are indicative; verify on Groww for latest figures.
FAQ_DATA = {
    "HDFC Mid-Cap Opportunities Fund": {
        "source_url": "https://groww.in/mutual-funds/hdfc-mid-cap-opportunities-fund-direct-plan-growth",
        "faqs": [
            {
                "q": "What is the expense ratio of HDFC Mid-Cap Opportunities Fund (Direct)?",
                "a": (
                    "The expense ratio for the Direct Plan is approximately 0.78% per annum. "
                    "This is deducted from the fund's NAV and is lower than the Regular Plan. "
                    "Check Groww for the latest figure as it is reviewed periodically."
                ),
            },
            {
                "q": "What is the exit load on HDFC Mid-Cap Opportunities Fund?",
                "a": (
                    "Exit load is 1% if units are redeemed or switched out within 1 year from the "
                    "date of allotment. No exit load applies after 1 year."
                ),
            },
        ],
    },
    "HDFC Top 100 Fund (Large Cap)": {
        "source_url": "https://groww.in/mutual-funds/hdfc-top-100-fund-direct-plan-growth",
        "faqs": [
            {
                "q": "What is the benchmark index for HDFC Top 100 Fund?",
                "a": (
                    "HDFC Top 100 Fund benchmarks against the NIFTY 100 Total Return Index (TRI). "
                    "The TRI includes reinvested dividends, making it a stricter benchmark than a "
                    "price-only index."
                ),
            },
            {
                "q": "Who manages HDFC Top 100 Fund?",
                "a": (
                    "The fund is managed by Rahul Baijal (primary) and Priya Ranjan (co-manager). "
                    "Fund manager details can change; confirm the current manager on the Groww scheme page."
                ),
            },
        ],
    },
    "HDFC Small Cap Fund": {
        "source_url": "https://groww.in/mutual-funds/hdfc-small-cap-fund-direct-plan-growth",
        "faqs": [
            {
                "q": "What is the minimum SIP amount for HDFC Small Cap Fund?",
                "a": (
                    "The minimum SIP investment is ₹100 per month with no upper limit. "
                    "The minimum lumpsum investment is also ₹100."
                ),
            },
            {
                "q": "What is the investment objective of HDFC Small Cap Fund?",
                "a": (
                    "The fund aims to provide long-term capital appreciation by investing predominantly "
                    "in small-cap companies — i.e., companies ranked 251st and beyond in terms of "
                    "full market capitalisation. It follows a bottom-up stock selection approach."
                ),
            },
        ],
    },
    "HDFC Gold Fund of Fund": {
        "source_url": "https://groww.in/mutual-funds/hdfc-gold-fund-of-fund-direct-plan-growth",
        "faqs": [
            {
                "q": "What does HDFC Gold Fund of Fund invest in?",
                "a": (
                    "HDFC Gold Fund of Fund (FoF) invests in units of HDFC Gold ETF, which in turn "
                    "holds physical gold. It allows investors to get gold exposure without a demat "
                    "account, since it is structured as a Fund of Fund."
                ),
            },
            {
                "q": "Is there an exit load on HDFC Gold Fund of Fund?",
                "a": (
                    "Yes. An exit load of 1% applies if units are redeemed within 15 days of allotment. "
                    "No exit load is charged after 15 days."
                ),
            },
        ],
    },
    "HDFC Defence Fund": {
        "source_url": "https://groww.in/mutual-funds/hdfc-defence-fund-direct-plan-growth",
        "faqs": [
            {
                "q": "What is the category of HDFC Defence Fund?",
                "a": (
                    "HDFC Defence Fund is a Sectoral / Thematic fund. It invests primarily in companies "
                    "engaged in or benefiting from India's defence sector, including defence manufacturing, "
                    "aerospace, and related ancillaries. Sectoral funds carry higher concentration risk "
                    "than diversified funds."
                ),
            },
            {
                "q": "What is the minimum lumpsum investment in HDFC Defence Fund?",
                "a": (
                    "The minimum lumpsum investment is ₹100. The minimum SIP amount is also ₹100 per month. "
                    "There is no upper limit on investment amount."
                ),
            },
        ],
    },
}

ADVISORY_KEYWORDS = [
    "should i", "should i invest", "is it good", "is it better", "recommend",
    "which is best", "compare", "vs", "versus", "buy", "sell", "better than",
    "worth investing", "safe to invest", "will it give", "returns expected",
]

# ── Helpers ───────────────────────────────────────────────────────────────────
def is_advisory(query: str) -> bool:
    q = query.lower()
    return any(kw in q for kw in ADVISORY_KEYWORDS)

def find_answer(query: str):
    q = query.lower()
    for scheme, data in FAQ_DATA.items():
        for pair in data["faqs"]:
            if any(word in q for word in pair["q"].lower().split() if len(word) > 4):
                return scheme, pair["q"], pair["a"], data["source_url"]
    return None, None, None, None

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("📊 HDFC Mutual Fund FAQ")
st.caption("Facts only · Groww-sourced · No investment advice")

st.warning(
    "**Disclaimer:** This tool provides factual information only. "
    "Nothing here is investment advice. Mutual fund investments are subject to market risks. "
    "Please read all scheme-related documents carefully before investing.",
    icon="⚠️",
)

st.divider()

# ── Mode selector ─────────────────────────────────────────────────────────────
mode = st.radio(
    "How would you like to browse?",
    ["Browse by scheme", "Search a question"],
    horizontal=True,
)

st.divider()

# ── Browse mode ───────────────────────────────────────────────────────────────
if mode == "Browse by scheme":
    scheme = st.selectbox("Select a scheme:", list(FAQ_DATA.keys()))
    data = FAQ_DATA[scheme]

    st.markdown(
        f"**Source:** [View on Groww]({data['source_url']})",
        unsafe_allow_html=False,
    )
    st.markdown("")

    for pair in data["faqs"]:
        with st.expander(pair["q"]):
            st.markdown(pair["a"])
            st.markdown(
                f"📎 **Source:** [{scheme} on Groww]({data['source_url']})"
            )

# ── Search mode ───────────────────────────────────────────────────────────────
else:
    query = st.text_input(
        "Ask a factual question about an HDFC mutual fund:",
        placeholder="e.g. What is the exit load on HDFC Mid-Cap Opportunities Fund?",
    )

    if query:
        if is_advisory(query):
            st.error(
                "⛔ This question asks for investment advice or a comparison. "
                "This tool answers factual questions only (expense ratio, exit load, "
                "objective, benchmark, minimum investment). "
                "For advice, please consult a SEBI-registered investment advisor."
            )
        else:
            scheme, matched_q, answer, source_url = find_answer(query)
            if answer:
                st.success("**Answer found**")
                st.markdown(f"**Q:** {matched_q}")
                st.markdown(f"**A:** {answer}")
                st.markdown(f"📎 **Source:** [{scheme} on Groww]({source_url})")
            else:
                st.info(
                    "No match found in the current FAQ set. "
                    "Try browsing by scheme, or rephrase your question using terms like "
                    "'expense ratio', 'exit load', 'benchmark', 'fund manager', or 'minimum investment'."
                )

# ── Footer ────────────────────────────────────────────────────────────────────
st.divider()
st.caption(
    "Data sourced from Groww · Expense ratios and AUM are indicative and subject to change · "
    "v0.1 prototype — hardcoded FAQ · Not affiliated with HDFC AMC or Groww"
)
