"""
Gráficos de líneas temporales.
"""

import pandas as pd
import plotly.graph_objects as go
from .css import COLORS, LINE_LAYOUT, LINE_STYLE, MARKER_STYLE, get_legend_right


def create_evolution_chart(
    df: pd.DataFrame,
    date_col: str = 'Fecha',
    metrics: list = None,
    colors: list = None,
    title: str = 'Evolución de Usuarios',
    x_title: str = 'Fecha',
    y_title: str = 'Usuarios',
    height: int = 450,
    show_markers: bool = True,
    date_format: str = '%d/%m',
    dtick: str = 'D2'
) -> go.Figure:
    """
    Crea un gráfico de líneas de evolución temporal.
    """
    if metrics is None:
        metrics = ['Intención de Registro', 'Registro']
    
    if colors is None:
        colors = [COLORS["primary"], COLORS["secondary"]]
    
    fig = go.Figure()
    
    mode = 'lines+markers' if show_markers else 'lines'
    
    for i, metric in enumerate(metrics):
        trace_config = {
            "x": df[date_col],
            "y": df[metric],
            "mode": mode,
            "name": metric,
            "line": dict(color=colors[i % len(colors)], **LINE_STYLE)
        }
        
        if show_markers:
            trace_config["marker"] = MARKER_STYLE
        
        fig.add_trace(go.Scatter(**trace_config))
    
    # Configurar layout
    layout_config = LINE_LAYOUT.copy()
    layout_config["xaxis"]["tickformat"] = date_format
    layout_config["xaxis"]["dtick"] = dtick
    
    fig.update_layout(
        title=f'📈 {title}',
        xaxis_title=x_title,
        yaxis_title=y_title,
        height=height,
        legend=get_legend_right(),
        **layout_config
    )
    
    return fig
