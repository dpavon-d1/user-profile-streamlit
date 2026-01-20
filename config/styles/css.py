"""
Estilos CSS globales para Streamlit.
CSS específico de componentes está en cada módulo.
"""


def get_all_css():
    """Retorna CSS global para el dashboard."""
    return """
<style>
/* === ST.INFO TRANSPARENTE === */
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

/* === OCULTAR ÍNDICE EN DATAFRAMES === */
.dataframe tbody th {
    display: none;
}

/* === AJUSTES GENERALES === */
.stPlotlyChart {
    margin-bottom: 0 !important;
}
</style>
"""
