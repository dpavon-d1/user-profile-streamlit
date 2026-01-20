"""
Gráficos de líneas temporales.
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
    Crea un gráfico de líneas genérico.
    
    Args:
        df: DataFrame con los datos
        x_col: Columna para eje X
        y_cols: Lista de columnas para eje Y (cada una será una línea)
        colors: Lista de colores para cada línea
        title: Título del gráfico
        x_title: Título eje X
        y_title: Título eje Y
        height: Altura en pixels
        show_markers: Si True, muestra marcadores en la línea
        date_format: Formato de fecha para eje X (ej: '%d/%m')
        dtick: Intervalo de ticks (ej: 'D2' para cada 2 días)
        show_legend: Si True, muestra la leyenda
        
    Returns:
        Figura de Plotly
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
    
    # Configurar layout base
    layout_config = LINE_LAYOUT.copy()
    
    # Configurar formato de fecha si se especifica
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
