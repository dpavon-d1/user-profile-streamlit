"""
CSS styles and visual configuration for line charts.
"""

from config.styles.colors import hex_to_rgba

# === OPACITY FOR LINE CHARTS ===
LINE_OPACITY = 0.85

# === LINE COLORS (with opacity) ===
COLORS = {
    "primary": hex_to_rgba("#F28322", LINE_OPACITY),      # Orange (Intention)
    "secondary": hex_to_rgba("#2450A6", LINE_OPACITY),    # Blue (Registration)
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

