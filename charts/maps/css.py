"""
CSS styles and visual configuration for map charts.
"""

# === MAP COLORS ===
COLORS = {
    "primary": "#F28322",
    "primary_dark": "#A64724",
    "primary_light": "#F2C6A5",
    "border": "#cccccc",
    "land": "#f5f5f5"
}

# === CHOROPLETH COLOR SCALE ===
MAP_COLORSCALE = [[0, '#F2C6A5'], [0.5, '#F28322'], [1, '#A64724']]

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

