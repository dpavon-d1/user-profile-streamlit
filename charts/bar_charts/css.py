"""
CSS styles and visual configuration for bar charts.
"""

from config.styles.colors import hex_to_rgba, DEFAULT_OPACITY

# === OPACITY FOR BAR CHARTS ===
BAR_OPACITY = DEFAULT_OPACITY# Adjust this value (0-1) for bar chart opacity

# === BAR COLORS (with opacity) ===
COLORS = {
    "primary": hex_to_rgba("#F28322", BAR_OPACITY),
    "primary_dark": hex_to_rgba("#2450A6", BAR_OPACITY),
    "secondary": hex_to_rgba("#E682FA", BAR_OPACITY),
    "secondary_light": hex_to_rgba("#4E8ACF", BAR_OPACITY),
    "background": "#ffffff",
    "grid": "#e0e0e0"
}

DEFAULT_COLORS = [COLORS["primary"], COLORS["primary_dark"], COLORS["secondary"], COLORS["secondary_light"]]

# === BAR LAYOUT ===
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

# === HORIZONTAL LEGEND ===
def get_legend_horizontal():
    """Returns centered horizontal legend configuration."""
    return {
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "center",
        "x": 0.5
    }

