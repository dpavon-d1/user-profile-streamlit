"""
Estilos CSS y configuración visual para gráficos de funnel.
"""

# === COLORES FUNNEL ===
FUNNEL_COLORS = ["#2450A6", "#1565C0", "#4E8ACF"]
CONNECTOR_COLOR = "#A6C6ED"

# === LAYOUT FUNNEL ===
FUNNEL_LAYOUT = {
    "margin": {"l": 120, "r": 20, "t": 60, "b": 20},
    "xaxis": {
        "showticklabels": False,
        "showgrid": False,
        "zeroline": False
    },
    "yaxis": {
        "tickfont": {"size": 11}
    }
}

# === MARKER CONFIG ===
FUNNEL_MARKER = {
    "line": {"width": 1, "color": "white"}
}

# === CONNECTOR CONFIG ===
FUNNEL_CONNECTOR = {
    "fillcolor": CONNECTOR_COLOR,
    "line": {"width": 0}
}

