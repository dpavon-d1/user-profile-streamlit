"""
Gráficos de mapas geográficos.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .css import MAP_COLORSCALE, COLORS, GEO_LAYOUT, COLORBAR_CONFIG, MAP_INTERACTION_CONFIG


def create_map(
    df: pd.DataFrame,
    locations_col: str,
    color_col: str,
    hover_name_col: str = None,
    hover_data_cols: list = None,
    title: str = '',
    height: int = 500,
    colorscale: list = None,
    projection: str = 'natural earth',
    show_colorbar: bool = True,
    colorbar_title: str = None
) -> go.Figure:
    """
    Crea un mapa choropleth genérico.
    
    Args:
        df: DataFrame con los datos
        locations_col: Columna con códigos ISO de países
        color_col: Columna para colorear el mapa
        hover_name_col: Columna para nombre en hover (opcional)
        hover_data_cols: Lista de columnas adicionales para hover
        title: Título del mapa
        height: Altura en pixels
        colorscale: Escala de colores personalizada
        projection: Tipo de proyección ('natural earth', 'equirectangular', etc.)
        show_colorbar: Si True, muestra la barra de colores
        colorbar_title: Título de la barra de colores
        
    Returns:
        Figura de Plotly
    """
    if colorscale is None:
        colorscale = MAP_COLORSCALE
    
    fig = px.choropleth(
        df,
        locations=locations_col,
        color=color_col,
        hover_name=hover_name_col,
        hover_data=hover_data_cols,
        color_continuous_scale=colorscale,
        projection=projection,
        title=title
    )
    
    # Configurar colorbar
    colorbar_config = COLORBAR_CONFIG.copy()
    if colorbar_title:
        colorbar_config["title"] = colorbar_title
    
    fig.update_layout(
        coloraxis_colorbar=colorbar_config if show_colorbar else dict(len=0),
        coloraxis_showscale=show_colorbar,
        geo=GEO_LAYOUT,
        height=height,
        margin=dict(l=0, r=0, t=50, b=0)
    )
    
    # Igualar bordes de países coloreados
    fig.update_traces(
        marker_line_color=COLORS["border"],
        marker_line_width=0.5
    )
    
    return fig


def get_map_config() -> dict:
    """
    Retorna configuración para desactivar interactividad del mapa.
    """
    return MAP_INTERACTION_CONFIG
