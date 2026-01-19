"""
Componentes de KPI Cards para Streamlit.
"""

import streamlit as st
from styles.css import metric_card_html


def render_single_kpi(title: str, value: str):
    """
    Renderiza una única card de KPI.
    
    Args:
        title: Título del KPI
        value: Valor a mostrar
    """
    st.markdown(metric_card_html(title, value), unsafe_allow_html=True)


def render_kpi_cards(kpis: dict, columns: int = 5):
    """
    Renderiza múltiples KPI cards en columnas.
    
    Args:
        kpis: Dict con {título: valor}
        columns: Número de columnas
    """
    cols = st.columns(columns)
    
    for i, (title, value) in enumerate(kpis.items()):
        with cols[i % columns]:
            render_single_kpi(title, value)


def render_kpi_row(kpi_data: dict) -> None:
    """
    Renderiza una fila de KPIs usando los datos del módulo data.
    
    Args:
        kpi_data: Dict retornado por get_kpi_data()
    """

    if kpi_data is None or len(kpi_data.keys()) == 0:
        return

    render_kpi_cards(kpi_data, columns=5)

