"""
CSS styles and visual configuration for funnel charts.
"""

from config.styles.colors import hex_to_rgba, apply_opacity

# === OPACITY FOR FUNNEL CHARTS ===
FUNNEL_OPACITY = 0.85

# === FUNNEL COLORS (with opacity) ===
FUNNEL_COLORS = apply_opacity(["#2450A6", "#1565C0", "#4E8ACF"], FUNNEL_OPACITY)
CONNECTOR_COLOR = hex_to_rgba("#A6C6ED", 0.6)

# === FUNNEL LAYOUT ===
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

