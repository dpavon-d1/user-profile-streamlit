"""
CSS styles and visual configuration for funnel charts.
"""

from config.styles.colors import hex_to_rgba

# === OPACITY FOR FUNNEL CHARTS ===
FUNNEL_OPACITY = 0.85

# === FUNNEL COLORS (with opacity) ===
COLORS = {
    "primary": hex_to_rgba("#2450A6", FUNNEL_OPACITY),
    "primary_dark": hex_to_rgba("#1565C0", FUNNEL_OPACITY),
    "secondary": hex_to_rgba("#4E8ACF", FUNNEL_OPACITY),
    "connector": hex_to_rgba("#A6C6ED", 0.6)
}

FUNNEL_COLORS = [COLORS["primary"], COLORS["primary_dark"], COLORS["secondary"]]
CONNECTOR_COLOR = COLORS["connector"]

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

