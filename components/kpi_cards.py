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
    cards = []
    for title, value in kpis.items():
        cards.append(f'<div class="metric-card"><h3>{title}</h3><p>{value}</p></div>')
    
    # HTML completo con estilos inline para asegurar renderizado
    html = f'''
    <style>
    .kpi-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin-bottom: 16px;
        width: 100%;
    }}
    .metric-card {{
        background-color: #ffffff;
        border-radius: 8px;
        padding: 12px 20px;
        box-shadow: 0 4px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #F28322;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-width: 150px;
    }}
    .metric-card h3 {{
        color: #666666;
        font-size: 12px;
        font-weight: 500;
        margin: 0 0 6px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }}
    .metric-card p {{
        color: #1a1a1a;
        font-size: 22px;
        font-weight: 700;
        margin: 0;
        line-height: 1;
        white-space: nowrap;
    }}
    </style>
    <div class="kpi-container">{" ".join(cards)}</div>
    '''
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

