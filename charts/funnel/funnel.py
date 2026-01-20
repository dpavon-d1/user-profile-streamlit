"""
Conversion funnel charts.
"""

import numpy as np
import plotly.graph_objects as go
from .css import FUNNEL_COLORS, FUNNEL_LAYOUT, FUNNEL_MARKER, FUNNEL_CONNECTOR, FUNNEL_TEXT


def create_funnel_chart(
    etapas: list,
    valores: list,
    title: str = "Conversion Funnel",
    height: int = 500,
    use_log_scale: bool = True,
    subtitle: str = None
) -> go.Figure:
    """
    Create a funnel chart with optional logarithmic scale.
    
    Args:
        etapas: List of stage names
        valores: List of values per stage
        title: Chart title
        subtitle: Chart subtitle (optional)
        height: Height in pixels
        use_log_scale: If True, applies logarithmic scale
        
    Returns:
        Plotly Figure
    """
    # Calculate percentages relative to total (first stage)
    pct_initial = [(v / valores[0]) * 100 for v in valores]
    
    # Create custom labels
    textos_personalizados = [
        f"{v:,}<br>{p:.2f}%" if p < 100 else f"{v:,}" 
        for v, p in zip(valores, pct_initial)
    ]
    
    # Values for the chart (with or without log scale)
    x_values = np.log10(valores) if use_log_scale else valores
    
    # Configure marker with colors
    marker_config = FUNNEL_MARKER.copy()
    marker_config["color"] = FUNNEL_COLORS[:len(etapas)]
    
    fig = go.Figure(go.Funnel(
        y=etapas,
        x=x_values,
        text=textos_personalizados,
        textinfo="text",
        textposition="inside",
        insidetextanchor="middle",
        textfont=FUNNEL_TEXT,
        marker=marker_config,
        connector=FUNNEL_CONNECTOR,
        hoverinfo="y+text"
    ))

    # Title with or without subtitle
    if subtitle:
        fig.update_layout(
            title={"text": f"<b>{title}</b><br><span style='font-size:12px'>{subtitle}</span>"}
        )
    else:
        fig.update_layout(
            title={"text": f"<b>{title}</b>"}
        )
    
    # Apply layout from css.py
    fig.update_layout(
        **FUNNEL_LAYOUT,
        height=height
    )
    
    return fig
