"""
CSS styles and visual configuration for bar charts.
"""

from config.styles.colors import hex_to_rgba, apply_opacity, DEFAULT_OPACITY

# === OPACITY FOR BAR CHARTS ===
BAR_OPACITY = 0.85  # Adjust this value (0-1) for bar chart opacity

# === BAR COLORS (with opacity) ===
COLORS = {
    "primary": hex_to_rgba("#F28322", BAR_OPACITY),
    "primary_dark": hex_to_rgba("#A64724", BAR_OPACITY),
    "secondary": hex_to_rgba("#2450A6", BAR_OPACITY),
    "secondary_light": hex_to_rgba("#4E8ACF", BAR_OPACITY),
    "background": "#ffffff",
    "grid": "#e0e0e0"
}

DEFAULT_COLORS = apply_opacity(['#A64724', '#F28322', '#33AAFF', '#2450A6'], BAR_OPACITY)

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

# === SESSION HISTORY SPECIFIC CONFIG ===
SESSION_HISTORY_CONFIG = {
    "bargap": 0.5,
    "bargroupgap": 0.02,
    "bar_width": 0.25
}

