"""
Gráficos de mapas geográficos.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from .css import MAP_COLORSCALE, COLORS, GEO_LAYOUT, COLORBAR_CONFIG, MAP_INTERACTION_CONFIG


def create_choropleth_map(
    df: pd.DataFrame,
    locations_col: str = 'ISO',
    color_col: str = 'Registros',
    hover_name_col: str = 'Pais',
    hover_data_cols: list = None,
    title: str = 'Registros e Intención por País',
    height: int = 500,
    colorscale: list = None
) -> go.Figure:
    """
    Crea un mapa choropleth.
    """
    if hover_data_cols is None:
        hover_data_cols = ['Intención', 'Registros']
    
    if colorscale is None:
        colorscale = MAP_COLORSCALE
    
    fig = px.choropleth(
        df,
        locations=locations_col,
        color=color_col,
        hover_name=hover_name_col,
        hover_data=hover_data_cols,
        color_continuous_scale=colorscale,
        projection='natural earth',
        title=title
    )
    
    fig.update_layout(
        coloraxis_colorbar=COLORBAR_CONFIG,
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
