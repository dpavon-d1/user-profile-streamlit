"""
Gráficos de barras.
"""

import pandas as pd
import plotly.graph_objects as go
from .css import DEFAULT_COLORS, COLORS, BAR_LAYOUT, get_legend_horizontal, SESSION_HISTORY_CONFIG


def create_bar_chart(
    df: pd.DataFrame,
    dimension_x_axis: str,
    dimension_col: str,
    breakdown_col: str,
    title: str = '',
    height: int = 400,
    colors: list = None,
    barmode: str = 'group'
) -> go.Figure:
    """
    Crea un gráfico de barras.
    """
    if colors is None:
        colors = DEFAULT_COLORS
    
    fig = go.Figure()
    
    for i, row in df.iterrows():
        fig.add_trace(go.Bar(
            name=row[dimension_x_axis],
            x=[dimension_col, breakdown_col],
            y=[row[dimension_col], row[breakdown_col]],
            marker_color=colors[i % len(colors)] if colors else None
        ))
    
    fig.update_layout(
        barmode=barmode,
        title=title,
        legend=get_legend_horizontal(),
        height=height,
        **BAR_LAYOUT
    )
    
    return fig


def create_stacked_bar_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: list,
    colors: list = None,
    title: str = '',
    x_title: str = '',
    y_title: str = 'Usuarios',
    height: int = 450,
    rotate_labels: bool = False,
    barmode: str = 'group'
) -> go.Figure:
    """
    Crea un gráfico de barras agrupadas genérico.
    """
    if colors is None:
        colors = [COLORS["secondary"], COLORS["primary"]]
    
    fig = go.Figure()
    
    for i, col in enumerate(y_cols):
        fig.add_trace(go.Bar(
            name=col,
            x=df[x_col],
            y=df[col],
            marker_color=colors[i % len(colors)]
        ))
    
    xaxis_config = {
        "showgrid": False,
        "title": x_title
    }
    
    if rotate_labels:
        xaxis_config["tickangle"] = -45
    
    fig.update_layout(
        title=title,
        xaxis=xaxis_config,
        yaxis={
            "title": y_title,
            "showgrid": True,
            "gridcolor": COLORS["grid"],
            "gridwidth": 1
        },
        barmode=barmode,
        height=height,
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        legend=get_legend_horizontal()
    )
    
    return fig
