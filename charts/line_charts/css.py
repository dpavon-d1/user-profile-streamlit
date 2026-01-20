"""
Estilos CSS y configuración visual para gráficos de líneas.
"""

# === COLORES LÍNEAS ===
COLORS = {
    "primary": "#F28322",      # Naranja (Intención)
    "secondary": "#2450A6",    # Azul (Registro)
    "background": "#ffffff",
    "grid": "#e0e0e0"
}

# === LAYOUT LÍNEAS ===
LINE_LAYOUT = {
    "plot_bgcolor": COLORS["background"],
    "paper_bgcolor": COLORS["background"],
    "hovermode": "x unified",
    "xaxis": {
        "showgrid": False,
        "tickformat": "%d/%m",
        "dtick": "D2"
    },
    "yaxis": {
        "showgrid": True,
        "gridcolor": COLORS["grid"],
        "gridwidth": 1
    }
}

# === LEYENDA DERECHA ===
def get_legend_right():
    """Retorna configuración de leyenda horizontal a la derecha."""
    return {
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "right",
        "x": 1
    }

# === ESTILO LÍNEAS ===
LINE_STYLE = {
    "width": 2
}

# === ESTILO MARKERS ===
MARKER_STYLE = {
    "size": 5
}

