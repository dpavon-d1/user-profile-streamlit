"""
Estilos CSS y configuración visual para heatmaps y tablas con gradientes.
"""

from matplotlib.colors import LinearSegmentedColormap

# === ESCALA HEATMAP PLOTLY ===
HEATMAP_COLORSCALE = [[0, '#FEF0E3'], [0.5, '#F9B86C'], [1, '#F28322']]

# === LAYOUT HEATMAP ===
HEATMAP_LAYOUT = {
    "yaxis": {"autorange": "reversed"}  # Primera fila arriba
}

# === TEXT TEMPLATE ===
TEXT_CONFIG = {
    "texttemplate": "%{text:,.0f}",
    "textfont": {"size": 12}
}

# === HOVER TEMPLATE ===
HOVER_CONFIG = {
    "hovertemplate": "%{y}<br>%{x}: %{z:,.0f}<extra></extra>"
}


# === COLORMAPS PARA PANDAS STYLE ===
def get_cmap_naranja():
    """Colormap naranja para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('naranja', ['#FEF0E3', '#E38766', '#A64724'])

def get_cmap_azul():
    """Colormap azul para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('azul', ['#E3F0FE', '#4E8ACF', '#2450A6'])

def get_cmap_purpura():
    """Colormap púrpura/naranja para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('purpura', ['#FFF1E5', '#F5A964', '#F28322'])


# === CONFIGURACIÓN POR DEFECTO DE COLUMNAS ===
DEFAULT_COLUMN_CMAPS = {
    'Usuarios': 'azul',
    'Intención de Registro': 'naranja',
    'Registrados': 'purpura'
}

