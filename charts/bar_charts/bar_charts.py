"""
Bar charts.
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
    Create a bar chart.
    
    Args:
        df: DataFrame with the data
        dimension_x_axis: Column for x-axis dimension
        dimension_col: First metric column
        breakdown_col: Second metric column
        title: Chart title
        height: Height in pixels
        colors: List of colors for bars
        barmode: Bar mode ('group' or 'stack')
        
    Returns:
        Plotly Figure
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
    y_title: str = 'Users',
    height: int = 450,
    rotate_labels: bool = False,
    barmode: str = 'group'
) -> go.Figure:
    """
    Create a generic grouped/stacked bar chart.
    
    Args:
        df: DataFrame with the data
        x_col: Column for x-axis
        y_cols: List of columns for y-axis (each will be a bar series)
        colors: List of colors for each series
        title: Chart title
        x_title: X-axis title
        y_title: Y-axis title
        height: Height in pixels
        rotate_labels: If True, rotates x-axis labels 45 degrees
        barmode: Bar mode ('group' or 'stack')
        
    Returns:
        Plotly Figure
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
