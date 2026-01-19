"""
Gráficos de líneas temporales.
"""

import pandas as pd
import plotly.graph_objects as go
from styles.colors import COLORS, get_legend_horizontal


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
    
    Args:
        df: DataFrame con los datos
        date_col: Columna de fechas
        metrics: Lista de columnas métricas a graficar
        colors: Lista de colores para cada métrica
        title: Título del gráfico
        x_title: Título eje X
        y_title: Título eje Y
        height: Altura en pixels
        show_markers: Si True, muestra marcadores en la línea
        date_format: Formato de fecha para el eje X
        dtick: Intervalo de ticks
        
    Returns:
        Figura de Plotly
    """
    if metrics is None:
        metrics = ['Intención de Registro', 'Registro']
    
    if colors is None:
        colors = [COLORS["primary"], COLORS["secondary"]]
    
    fig = go.Figure()
    
    mode = 'lines+markers' if show_markers else 'lines'
    
    for i, metric in enumerate(metrics):
        fig.add_trace(go.Scatter(
            x=df[date_col],
            y=df[metric],
            mode=mode,
            name=metric,
            line=dict(color=colors[i % len(colors)], width=2),
            marker=dict(size=5) if show_markers else None
        ))
    
    legend_config = get_legend_horizontal()
    legend_config['xanchor'] = 'right'
    legend_config['x'] = 1
    
    fig.update_layout(
        title=f'📈 {title}',
        xaxis_title=x_title,
        yaxis_title=y_title,
        height=height,
        hovermode='x unified',
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"],
        legend=legend_config,
        xaxis=dict(
            tickformat=date_format,
            dtick=dtick,
            showgrid=False
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLORS["grid"],
            gridwidth=1
        )
    )
    
    return fig

