"""
Componentes de KPI Cards para Streamlit.
"""

import streamlit as st
from styles.css import metric_card_html, kpi_container_html


def render_single_kpi(title: str, value: str):
    """
    Renderiza una única card de KPI.
    
    Args:
        title: Título del KPI
        value: Valor a mostrar
    """
    st.markdown(metric_card_html(title, value), unsafe_allow_html=True)


def render_kpi_cards(kpis: dict):
    """
    Renderiza múltiples KPI cards en columnas centradas.
    
    Args:
        kpis: Dict con {título: valor}
        columns: Número de columnas (no usado, se mantiene por compatibilidad)
    """
    # Generar HTML de todas las cards
    cards_html = ""
    for title, value in kpis.items():
        cards_html += f"""
        <div class="metric-card">
            <h3>{title}</h3>
            <p>{value}</p>
        </div>
        """
    
    # Renderizar contenedor centrado con todas las cards
    st.markdown(kpi_container_html(cards_html), unsafe_allow_html=True)


def render_kpi_row(kpi_data: dict) -> None:
    """
    Renderiza una fila de KPIs usando los datos del módulo data.
    
    Args:
        kpi_data: Dict retornado por get_kpi_data()
    """

    if kpi_data is None or len(kpi_data.keys()) == 0:
        return

    render_kpi_cards(kpi_data)

