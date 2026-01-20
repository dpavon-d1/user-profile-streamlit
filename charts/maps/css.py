"""
Estilos CSS y configuración visual para gráficos de mapas.
"""

# === COLORES MAPAS ===
COLORS = {
    "primary": "#F28322",
    "primary_dark": "#A64724",
    "primary_light": "#F2C6A5",
    "border": "#cccccc",
    "land": "#f5f5f5"
}

# === ESCALA DE COLOR CHOROPLETH ===
MAP_COLORSCALE = [[0, '#F2C6A5'], [0.5, '#F28322'], [1, '#A64724']]

# === LAYOUT GEO ===
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

# === COLORBAR HORIZONTAL ===
COLORBAR_CONFIG = {
    "orientation": "h",
    "thickness": 15,
    "title": "Usuarios",
    "yanchor": "top",
    "y": -0.05,
    "xanchor": "right",
    "x": 0.5,
    "len": 0.5
}

# === CONFIG INTERACTIVIDAD (para st.plotly_chart) ===
MAP_INTERACTION_CONFIG = {
    'scrollZoom': False,
    'doubleClick': False,
    'displayModeBar': False
}


# === CONFIGURACIÓN DE MAPA ===
MAP_CONFIG = {
    "scrollZoom": False,
    "doubleClick": False,
    "displayModeBar": False
}


