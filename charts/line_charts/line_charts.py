"""
Time series line charts.
"""

import pandas as pd
import plotly.graph_objects as go
from .css import COLORS, LINE_LAYOUT, LINE_STYLE, MARKER_STYLE, get_legend_right


def create_line_chart(
    df: pd.DataFrame,
    x_col: str,
    y_cols: list,
    colors: list = None,
    title: str = '',
    x_title: str = '',
    y_title: str = '',
    height: int = 450,
    show_markers: bool = True,
    date_format: str = None,
    dtick: str = None,
    show_legend: bool = True
) -> go.Figure:
    """
    Create a generic line chart.
    
    Args:
        df: DataFrame with the data
        x_col: Column for X axis
        y_cols: List of columns for Y axis (each will be a line)
        colors: List of colors for each line
        title: Chart title
        x_title: X axis title
        y_title: Y axis title
        height: Height in pixels
        show_markers: If True, shows markers on the line
        date_format: Date format for X axis (e.g.: '%d/%m')
        dtick: Tick interval (e.g.: 'D2' for every 2 days)
        show_legend: If True, shows the legend
        
    Returns:
        Plotly Figure
    """
    if colors is None:
        colors = [COLORS["primary"], COLORS["secondary"]]
    
    fig = go.Figure()
    
    mode = 'lines+markers' if show_markers else 'lines'
    
    for i, col in enumerate(y_cols):
        trace_config = {
            "x": df[x_col],
            "y": df[col],
            "mode": mode,
            "name": col,
            "line": dict(color=colors[i % len(colors)], **LINE_STYLE)
        }
        
        if show_markers:
            trace_config["marker"] = MARKER_STYLE
        
        fig.add_trace(go.Scatter(**trace_config))
    
    # Configure base layout
    layout_config = LINE_LAYOUT.copy()
    
    # Configure date format if specified
    if date_format:
        layout_config["xaxis"]["tickformat"] = date_format
    if dtick:
        layout_config["xaxis"]["dtick"] = dtick
    
    fig.update_layout(
        title=title,
        xaxis_title=x_title,
        yaxis_title=y_title,
        height=height,
        showlegend=show_legend,
        legend=get_legend_right() if show_legend else None,
        **layout_config
    )
    
    return fig
