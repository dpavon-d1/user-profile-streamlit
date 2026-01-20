"""
Gráficos de funnel de conversión.
"""

import numpy as np
import plotly.graph_objects as go
from .css import FUNNEL_COLORS, FUNNEL_LAYOUT, FUNNEL_MARKER, FUNNEL_CONNECTOR


def create_funnel_chart(
    etapas: list,
    valores: list,
    title: str = "Embudo de Conversión",
    height: int = 500,
    use_log_scale: bool = True,
    subtitle: str = None
) -> go.Figure:
    """
    Crea un gráfico de funnel con escala logarítmica opcional.
    
    Args:
        etapas: Lista de nombres de etapas
        valores: Lista de valores por etapa
        title: Título del gráfico
        subtitle: Subtítulo del gráfico (opcional)
        height: Altura en pixels
        use_log_scale: Si True, aplica escala logarítmica
        
    Returns:
        Figura de Plotly
    """
    # Calcular porcentajes respecto al total (primera etapa)
    pct_initial = [(v / valores[0]) * 100 for v in valores]
    
    # Crear etiquetas personalizadas
    textos_personalizados = [
        f"{v:,}<br>{p:.2f}%" if p < 100 else f"{v:,}" 
        for v, p in zip(valores, pct_initial)
    ]
    
    # Valores para el gráfico (con o sin escala log)
    x_values = np.log10(valores) if use_log_scale else valores
    
    # Configurar marker con colores
    marker_config = FUNNEL_MARKER.copy()
    marker_config["color"] = FUNNEL_COLORS[:len(etapas)]
    
    fig = go.Figure(go.Funnel(
        y=etapas,
        x=x_values,
        text=textos_personalizados,
        textinfo="text",
        textposition="inside",
        insidetextanchor="middle",
        marker=marker_config,
        connector=FUNNEL_CONNECTOR,
        hoverinfo="y+text"
    ))

    # Título con o sin subtítulo
    if subtitle:
        fig.update_layout(
            title={"text": f"<b>{title}</b><br><span style='font-size:12px'>{subtitle}</span>"}
        )
    else:
        fig.update_layout(
            title={"text": f"<b>{title}</b>"}
        )
    
    # Aplicar layout desde css.py
    fig.update_layout(
        **FUNNEL_LAYOUT,
        height=height
    )
    
    return fig
