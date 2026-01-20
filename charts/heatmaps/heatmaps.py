"""
Gráficos de heatmap y tablas con gradientes.
"""

import pandas as pd
import plotly.graph_objects as go
from .css import (
    HEATMAP_COLORSCALE, 
    HEATMAP_LAYOUT, 
    TEXT_CONFIG, 
    HOVER_CONFIG,
    get_cmap_naranja, 
    get_cmap_azul, 
    get_cmap_purpura,
    DEFAULT_COLUMN_CMAPS
)


def create_heatmap_table(
    df: pd.DataFrame,
    index_col: str,
    title: str = 'Heatmap',
    height: int = 400,
    colorscale: list = None,
    show_colorbar: bool = False
) -> go.Figure:
    """
    Crea un heatmap interactivo con Plotly.
    """
    if colorscale is None:
        colorscale = HEATMAP_COLORSCALE
    
    # Establecer índice
    df_indexed = df.set_index(index_col)
    
    fig = go.Figure(data=go.Heatmap(
        showscale=show_colorbar,
        z=df_indexed.values,
        x=df_indexed.columns,
        y=df_indexed.index,
        colorscale=colorscale,
        text=df_indexed.values,
        texttemplate=TEXT_CONFIG["texttemplate"],
        textfont=TEXT_CONFIG["textfont"],
        hovertemplate=HOVER_CONFIG["hovertemplate"]
    ))
    
    fig.update_layout(
        title=title,
        height=height,
        **HEATMAP_LAYOUT
    )
    
    return fig


def style_dataframe_heatmap(
    df: pd.DataFrame,
    columns_config: dict = None
):
    """
    Aplica estilos de heatmap a un DataFrame de Pandas.
    """
    # Mapeo de nombres a colormaps
    cmap_map = {
        'naranja': get_cmap_naranja(),
        'azul': get_cmap_azul(),
        'purpura': get_cmap_purpura()
    }
    
    # Configuración por defecto
    if columns_config is None:
        columns_config = DEFAULT_COLUMN_CMAPS
    
    # Aplicar gradientes
    styled = df.style
    
    for col, cmap_name in columns_config.items():
        if col in df.columns:
            styled = styled.background_gradient(
                subset=[col],
                cmap=cmap_map.get(cmap_name, get_cmap_naranja())
            )
    
    # Formatear números
    format_dict = {col: '{:,.0f}' for col in df.columns if df[col].dtype in ['int64', 'float64']}
    styled = styled.format(format_dict)
    
    return styled


def filter_top_n(df: pd.DataFrame, n: int, column: str) -> pd.DataFrame:
    """
    Filtra los top N registros de un DataFrame.
    """
    return df.nlargest(n, column)
