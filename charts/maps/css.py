"""
CSS styles and visual configuration for map charts.
"""

from config.styles.colors import hex_to_rgba

# === OPACITY FOR MAP CHARTS ===
MAP_OPACITY = 0.85

# === MAP COLORS (with opacity) ===
COLORS = {
    "primary": hex_to_rgba("#F28322", MAP_OPACITY),
    "primary_dark": hex_to_rgba("#A64724", MAP_OPACITY),
    "primary_light": hex_to_rgba("#F2C6A5", MAP_OPACITY),
    "border": "#cccccc",
    "land": "#f5f5f5"
}

# === CHOROPLETH COLOR SCALE (with opacity) ===
MAP_COLORSCALE = [
    [0, hex_to_rgba('#F2C6A5', MAP_OPACITY)], 
    [0.5, hex_to_rgba('#F28322', MAP_OPACITY)], 
    [1, hex_to_rgba('#A64724', MAP_OPACITY)]
]

# === GEO LAYOUT ===
GEO_LAYOUT = {
    "showframe": False,
    "showcoastlines": False,
    "showland": True,
    "landcolor": COLORS["land"],
    "showcountries": True,
    "countrycolor": COLORS["border"],
    "countrywidth": 0.5,
    "showlakes": False,
    "showrivers": False,
    "lataxis": {"showgrid": False},
    "lonaxis": {"showgrid": False},
    "showsubunits": False,
    "framewidth": 0
}

# === HORIZONTAL COLORBAR ===
COLORBAR_CONFIG = {
    "orientation": "h",
    "thickness": 15,
    "title": "Users",
    "yanchor": "top",
    "y": -0.05,
    "xanchor": "right",
    "x": 0.5,
    "len": 0.5
}

# === INTERACTION CONFIG (for st.plotly_chart) ===
MAP_INTERACTION_CONFIG = {
    'scrollZoom': False,
    'doubleClick': False,
    'displayModeBar': False
}

