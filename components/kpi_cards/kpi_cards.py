"""
Componentes de KPI Cards para Streamlit.
"""

import streamlit as st
from kpi_css import BASIC_CARD_CSS, CONTAINER_CSS

def render_kpi_cards(kpis: dict):
    """
    Renderiza múltiples KPI cards centradas usando flexbox.
    
    Args:
        kpis: Dict con {título: valor}
    """
    # Generar HTML de todas las cards
    cards = []
    for title, value in kpis.items():
        cards.append(BASIC_CARD_CSS.format(title=title, value=value))
    
    # HTML completo con estilos inline para asegurar renderizado
    html = CONTAINER_CSS.format(cards_html=" ".join(cards))
    st.markdown(html, unsafe_allow_html=True)


def render_kpi_row(kpi_data: dict) -> None:
    """
    Renderiza una fila de KPIs usando los datos del módulo data.
    
    Args:
        kpi_data: Dict retornado por get_kpi_data()
    """
    if kpi_data is None or len(kpi_data.keys()) == 0:
        return

    render_kpi_cards(kpi_data)

