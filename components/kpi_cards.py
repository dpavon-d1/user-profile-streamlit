"""
Componentes de KPI Cards para Streamlit.
"""

import streamlit as st


def render_kpi_cards(kpis: dict):
    """
    Renderiza múltiples KPI cards centradas usando flexbox.
    
    Args:
        kpis: Dict con {título: valor}
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
    
    # Contenedor flex que centra todas las cards
    html = f"""
    <div class="kpi-container">
        {cards_html}
    </div>
    """
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

