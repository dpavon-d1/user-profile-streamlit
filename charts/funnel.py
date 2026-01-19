"""
Gráficos de funnel de conversión.
"""

import numpy as np
import plotly.graph_objects as go
from styles.colors import FUNNEL_COLORS, COLORS


def create_funnel_chart(
    etapas: list,
    valores: list,
    title: str = "Embudo de Conversión",
    subtitle: str = "Escala logarítmica aplicada para visibilidad",
    height: int = 500,
    use_log_scale: bool = True
) -> go.Figure:
    """
    Crea un gráfico de funnel con escala logarítmica opcional.
    
    Args:
        etapas: Lista de nombres de etapas
        valores: Lista de valores por etapa
        title: Título del gráfico
        subtitle: Subtítulo del gráfico
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
    
    fig = go.Figure(go.Funnel(
        y=etapas,
        x=x_values,
        text=textos_personalizados,
        textinfo="text",
        textposition="inside",
        insidetextanchor="middle",
        marker={
            "color": FUNNEL_COLORS[:len(etapas)],
            "line": {"width": 1, "color": "white"}
        },
        connector={"fillcolor": "#A6C6ED", "line": {"width": 0}},
        hoverinfo="y+text"
    ))
    
    fig.update_layout(
        title={
            "text": f"<b>{title}</b><br><span style='font-size:12px'>{subtitle}</span>"
        },
        xaxis={
            "showticklabels": False,
            "showgrid": False,
            "zeroline": False
        },
        margin=dict(l=200),
        height=height
    )
    
    return fig

