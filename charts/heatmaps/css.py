"""
CSS styles and visual configuration for heatmaps and gradient tables.
"""

from matplotlib.colors import LinearSegmentedColormap
from config.styles.colors import hex_to_rgba

# === OPACITY FOR HEATMAP CHARTS ===
HEATMAP_OPACITY = 0.85

# === PLOTLY HEATMAP COLOR SCALE (with opacity) ===
HEATMAP_COLORSCALE = [
    [0, hex_to_rgba('#FEF0E3', HEATMAP_OPACITY)], 
    [0.5, hex_to_rgba('#F9B86C', HEATMAP_OPACITY)], 
    [1, hex_to_rgba('#F28322', HEATMAP_OPACITY)]
]

# === HEATMAP LAYOUT ===
HEATMAP_LAYOUT = {
    "yaxis": {"autorange": "reversed"}  # First row on top
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


# === COLORMAPS FOR PANDAS STYLE ===
def get_cmap_naranja():
    """Orange colormap for table gradients."""
    return LinearSegmentedColormap.from_list('naranja', ['#FEF0E3', '#E38766', '#A64724'])

def get_cmap_azul():
    """Blue colormap for table gradients."""
    return LinearSegmentedColormap.from_list('azul', ['#E3F0FE', '#4E8ACF', '#2450A6'])

def get_cmap_purpura():
    """Purple/orange colormap for table gradients."""
    return LinearSegmentedColormap.from_list('purpura', ['#FFF1E5', '#F5A964', '#F28322'])


# === DEFAULT COLUMN CONFIGURATION ===
DEFAULT_COLUMN_CMAPS = {
    'Usuarios': 'azul',
    'Intención de Registro': 'naranja',
    'Registrados': 'purpura'
}

