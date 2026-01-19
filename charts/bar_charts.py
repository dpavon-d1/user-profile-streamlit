"""
Gráficos de barras.
"""

import pandas as pd
import plotly.graph_objects as go
from styles.colors import DEVICE_COLORS, COLORS, get_legend_horizontal


def create_device_bar_chart(
    df: pd.DataFrame,
    device_col: str = 'Dispositivo',
    registered_col: str = 'Registrado',
    intention_col: str = 'Con Intención',
    title: str = 'Según Dispositivo y Estado',
    height: int = 400,
    colors: list = None,
    barmode: str = 'group'
) -> go.Figure:
    """
    Crea un gráfico de barras agrupadas por dispositivo.
    
    Args:
        df: DataFrame con los datos
        device_col: Columna de dispositivos
        registered_col: Columna de registrados
        intention_col: Columna de intención
        title: Título del gráfico
        height: Altura en pixels
        colors: Lista de colores por dispositivo
        
    Returns:
        Figura de Plotly
    """
    if colors is None:
        colors = DEVICE_COLORS
    
    estados = [registered_col, intention_col]
    
    fig = go.Figure()
    
    for i, row in df.iterrows():
        fig.add_trace(go.Bar(
            name=row[device_col],
            x=estados,
            y=[row[registered_col], row[intention_col]],
            marker_color=colors[i % len(colors)]
        ))
    
    fig.update_layout(
        barmode='group',
        title=title,
        legend=get_legend_horizontal(),
        height=height,
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"]
    )
    
    return fig


def create_session_history_chart(
    df: pd.DataFrame,
    type_col: str = 'Tipo Usuario',
    registered_col: str = 'Registrado',
    intention_col: str = 'Con Intención',
    title: str = 'Según historial de sesiones',
    height: int = 400,
    bar_width: float = 0.25,
    colors: list = None
) -> go.Figure:
    """
    Crea un gráfico de barras por historial de sesiones.
    
    Args:
        df: DataFrame con los datos
        type_col: Columna de tipo de usuario
        registered_col: Columna de registrados
        intention_col: Columna de intención
        title: Título del gráfico
        height: Altura en pixels
        bar_width: Ancho de las barras
        colors: Lista de colores
        
    Returns:
        Figura de Plotly
    """
    if colors is None:
        colors = DEVICE_COLORS
    
    estados = [registered_col, intention_col]
    
    fig = go.Figure()
    
    for i, row in df.iterrows():
        fig.add_trace(go.Bar(
            name=row[type_col],
            x=estados,
            y=[row[registered_col], row[intention_col]],
            marker_color=colors[i % len(colors)],
            width=bar_width
        ))
    
    fig.update_layout(
        barmode='group',
        title=title,
        bargap=0.5,
        bargroupgap=0.02,
        legend=get_legend_horizontal(),
        height=height,
        plot_bgcolor=COLORS["background"],
        paper_bgcolor=COLORS["background"]
    )
    
    return fig


def create_grouped_bar_chart(
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
    
    Args:
        df: DataFrame con los datos
        x_col: Columna para eje X
        y_cols: Lista de columnas para eje Y (cada una será una serie)
        colors: Lista de colores para cada serie
        title: Título del gráfico
        x_title: Título eje X
        y_title: Título eje Y
        height: Altura en pixels
        rotate_labels: Si True, rota etiquetas del eje X
        
    Returns:
        Figura de Plotly
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

