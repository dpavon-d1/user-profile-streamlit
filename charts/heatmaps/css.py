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


# === COLORMAPS FOR PANDAS STYLE (Source/Medium Table) ===
# Colors:
# - Usuarios: #2450A6 (Azul Infobae)
# - Intención de Registro: #FB8C00 (Naranja Medio)
# - Registrados: #E65100 (Naranja Fuerte - Sin transparencia)

def get_cmap_azul():
    """Blue colormap for 'Usuarios' column - Azul Infobae."""
    return LinearSegmentedColormap.from_list('azul', ['#EAF0FA', '#2E64D1', '#2450A6'])

def get_cmap_naranja():
    """Medium orange colormap for 'Intención de Registro' column."""
    return LinearSegmentedColormap.from_list('naranja', ['#EAF4FB', '#51A7DB', '#2B93D4'])

def get_cmap_exito():
    """Strong orange colormap for 'Registrados' column - SUCCESS (no transparency)."""
    return LinearSegmentedColormap.from_list('exito', ['#FEF1E7', '#F6A965', '#F39039'])


# === DEFAULT COLUMN CONFIGURATION ===
DEFAULT_COLUMN_CMAPS = {
    'Usuarios': 'azul',
    'Intención de Registro': 'naranja',
    'Registrados': 'exito'
}

