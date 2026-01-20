"""
CSS styles and visual configuration for line charts.
"""

# === LINE COLORS ===
COLORS = {
    "primary": "#F28322",      # Orange (Intention)
    "secondary": "#2450A6",    # Blue (Registration)
    "background": "#ffffff",
    "grid": "#e0e0e0"
}

# === LINE LAYOUT ===
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

# === RIGHT LEGEND ===
def get_legend_right():
    """Returns right-aligned horizontal legend configuration."""
    return {
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "right",
        "x": 1
    }

# === LINE STYLE ===
LINE_STYLE = {
    "width": 2
}

# === MARKER STYLE ===
MARKER_STYLE = {
    "size": 5
}

