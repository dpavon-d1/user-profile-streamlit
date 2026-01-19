"""
Paletas de colores y escalas de color para visualizaciones.
"""

from matplotlib.colors import LinearSegmentedColormap

# === COLORES PRINCIPALES ===
COLORS = {
    "primary": "#F28322",      # Naranja principal
    "primary_dark": "#A64724", # Naranja oscuro
    "primary_light": "#F2C6A5", # Naranja claro
    "secondary": "#2450A6",    # Azul principal
    "secondary_light": "#4E8ACF", # Azul claro
    "secondary_dark": "#1E43E6", # Azul oscuro
    "accent": "#1565C0",       # Azul acento
    "text_dark": "#1a1a1a",
    "text_medium": "#666666",
    "text_light": "#999999",
    "background": "#ffffff",
    "border": "#cccccc",
    "grid": "#e0e0e0"
}

# === PALETA PARA DISPOSITIVOS ===
DEVICE_COLORS = ['#A64724', '#F28322', 'rgb(51,153,255)', '#2450A6']

# === PALETA PARA FUNNEL ===
FUNNEL_COLORS = ["#2450A6", "#1565C0", "#4E8ACF"]

# === ESCALAS DE COLOR PARA MAPAS ===
MAP_COLORSCALE = [[0, '#F2C6A5'], [0.5, '#F28322'], [1, '#A64724']]

# === ESCALAS DE COLOR PARA HEATMAPS ===
HEATMAP_COLORSCALE = [[0, '#FEF0E3'], [0.5, '#F9B86C'], [1, '#F28322']]

# === COLORMAPS PARA TABLAS PANDAS ===
def get_cmap_naranja():
    """Colormap naranja para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('naranja', ['#FEF0E3', '#E38766', '#A64724'])

def get_cmap_azul():
    """Colormap azul para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('azul', ['#E3F0FE', '#4E8ACF', '#2450A6'])

def get_cmap_purpura():
    """Colormap púrpura/naranja para gradientes de tabla."""
    return LinearSegmentedColormap.from_list('purpura', ['#FFF1E5', '#F5A964', '#F28322'])

# === LAYOUT COMÚN PARA GRÁFICOS ===
def get_base_layout():
    """Retorna configuración base de layout para gráficos."""
    return {
        "plot_bgcolor": COLORS["background"],
        "paper_bgcolor": COLORS["background"],
        "font": {"family": "Arial, sans-serif"},
        "xaxis": {"showgrid": False},
        "yaxis": {
            "showgrid": True,
            "gridcolor": COLORS["grid"],
            "gridwidth": 1
        }
    }

def get_legend_horizontal():
    """Retorna configuración de leyenda horizontal centrada."""
    return {
        "orientation": "h",
        "yanchor": "bottom",
        "y": 1.02,
        "xanchor": "center",
        "x": 0.5
    }

