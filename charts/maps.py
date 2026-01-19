"""
Gráficos de mapas geográficos.
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from styles.colors import MAP_COLORSCALE, COLORS


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
    
    Args:
        df: DataFrame con los datos
        locations_col: Columna con códigos ISO de países
        color_col: Columna para colorear
        hover_name_col: Columna para nombre en hover
        hover_data_cols: Lista de columnas adicionales para hover
        title: Título del mapa
        height: Altura en pixels
        colorscale: Escala de colores personalizada
        
    Returns:
        Figura de Plotly
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
        coloraxis_colorbar=dict(
            orientation="h",
            thickness=15,
            title="Usuarios",
            yanchor="top",
            y=-0.05,
            xanchor="right",
            x=0.5,
            len=0.5
        ),
        geo=dict(
            showframe=False,
            showcoastlines=False,
            showland=True,
            landcolor='#f5f5f5',
            showcountries=True,
            countrycolor=COLORS["border"],
            countrywidth=0.5,
            showlakes=False,
            showrivers=False,
            lataxis=dict(showgrid=False),
            lonaxis=dict(showgrid=False),
            showsubunits=False,
            framewidth=0
        ),
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
    
    Returns:
        dict con configuración
    """
    return {
        'scrollZoom': False,
        'doubleClick': False,
        'displayModeBar': False
    }

