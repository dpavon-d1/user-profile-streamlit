"""
Estilos CSS y configuración visual para gráficos de barras.
"""

# === COLORES BARRAS ===
COLORS = {
    "primary": "#F28322",
    "primary_dark": "#A64724",
    "secondary": "#2450A6",
    "secondary_light": "#4E8ACF",
    "background": "#ffffff",
    "grid": "#e0e0e0"
}

DEFAULT_COLORS = ['#A64724', '#F28322', 'rgb(51,153,255)', '#2450A6']

# === LAYOUT BARRAS ===
BAR_LAYOUT = {
    "plot_bgcolor": COLORS["background"],
    "paper_bgcolor": COLORS["background"],
    "xaxis": {"showgrid": False},
    "yaxis": {
        "showgrid": True,
        "gridcolor": COLORS["grid"],
        "gridwidth": 1
    }
}

# === LEYENDA HORIZONTAL ===
def get_legend_horizontal():
    """Retorna configuración de leyenda horizontal centrada."""
    return {
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "center",
        "x": 0.5
    }

# === CONFIG ESPECÍFICO PARA HISTORIAL SESIONES ===
SESSION_HISTORY_CONFIG = {
    "bargap": 0.5,
    "bargroupgap": 0.02,
    "bar_width": 0.25
}

