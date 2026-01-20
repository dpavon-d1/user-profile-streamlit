"""
KPI Cards components for Streamlit.
"""

import streamlit as st
from .css import BASIC_CARD_CSS, CONTAINER_CSS


def render_kpi_cards(kpis: dict):
    """
    Render multiple KPI cards centered using flexbox.
    
    Args:
        kpis: Dict with {title: value}
    """
    # Generate HTML for all cards
    cards = []
    for title, value in kpis.items():
        cards.append(BASIC_CARD_CSS.format(title=title, value=value))
    
    # Complete HTML with inline styles to ensure rendering
    html = CONTAINER_CSS.format(cards_html=" ".join(cards))
    st.markdown(html, unsafe_allow_html=True)


def render_kpi_row(kpi_data: dict) -> None:
    """
    Render a row of KPIs using data from the data module.
    
    Args:
        kpi_data: Dict returned by get_kpi_data()
    """
    if kpi_data is None or len(kpi_data.keys()) == 0:
        return

    render_kpi_cards(kpi_data)

