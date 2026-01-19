"""
Estilos CSS para componentes de Streamlit.
"""

# === CSS PARA CARDS DE KPI ===
KPI_CARD_CSS = """
<style>
.metric-card {
    background-color: #ffffff;
    border-radius: 8px;
    padding: 10px 8px;
    box-shadow: 0 4px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #F28322;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.metric-card h3 {
    color: #666666;
    font-size: 14px;
    font-weight: 500;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
    width: 100%;
}
.metric-card p {
    color: #1a1a1a;
    font-size: 24px;
    font-weight: 700;
    margin: 0;
    line-height: 1;
    text-align: center;
    width: 100%;
}
</style>
"""

# === CSS PARA ST.INFO TRANSPARENTE ===
INFO_TRANSPARENT_CSS = """
<style>
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
</style>
"""

# === CSS COMBINADO (para cargar todo junto) ===
def get_all_css():
    """Retorna todo el CSS combinado para el dashboard."""
    return f"""
<style>
/* === CONTENEDOR KPI CARDS === */
.kpi-container {{
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 16px;
    margin-bottom: 16px;
}}

/* === METRIC CARDS === */
.metric-card {{
    background-color: #ffffff;
    border-radius: 8px;
    padding: 12px 16px;
    box-shadow: 0 4px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #F28322;
    display: inline-flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    margin-bottom: 12px;
    width: fit-content;
    min-width: 100%;
}}
.metric-card h3 {{
    color: #666666;
    font-size: 13px;
    font-weight: 500;
    margin: 0 0 6px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
    white-space: nowrap;
}}
.metric-card p {{
    color: #1a1a1a;
    font-size: 24px;
    font-weight: 700;
    margin: 0;
    line-height: 1;
    text-align: center;
    white-space: nowrap;
}}

/* === ST.INFO TRANSPARENTE === */
div[data-testid="stAlert"] {{
    background-color: transparent !important;
    border: none !important;
}}
div[data-testid="stAlert"] > div {{
    background-color: transparent !important;
}}
div[data-testid="stAlert"] p {{
    color: #000000 !important;
    font-size: 14px !important;
}}

/* === OCULTAR ÍNDICE EN DATAFRAMES === */
.dataframe tbody th {{
    display: none;
}}
</style>
"""

# === TEMPLATES HTML PARA CARDS ===
def metric_card_html(title: str, value: str) -> str:
    """Genera HTML para una card de métrica."""
    return f"""
    <div class="metric-card">
        <h3>{title}</h3>
        <p>{value}</p>
    </div>
    """

def kpi_container_html(cards_html: str) -> str:
    """Genera HTML para el contenedor de KPI cards centrado."""
    return f"""
    <div class="kpi-container">
        {cards_html}
    </div>
    """

