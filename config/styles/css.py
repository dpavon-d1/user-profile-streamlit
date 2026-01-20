"""
Global CSS styles for Streamlit.
Component-specific CSS is in each module.
"""


def get_all_css():
    """Returns global CSS for the dashboard."""
    return """
<style>
/* === TRANSPARENT ST.INFO === */
div[data-testid="stAlert"] {
    background-color: transparent !important;
    border: none !important;
}
div[data-testid="stAlert"] > div {
    background-color: transparent !important;
}
div[data-testid="stAlert"] p {
    color: #000000 !important;
    font-size: 14px !important;
}

/* === HIDE DATAFRAME INDEX === */
.dataframe tbody th {
    display: none;
}

/* === GENERAL ADJUSTMENTS === */
.stPlotlyChart {
    margin-bottom: 0 !important;
}
</style>
"""
