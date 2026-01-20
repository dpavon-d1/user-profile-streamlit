"""
Componentes de filtros para sidebar de Streamlit.
"""

import streamlit as st
from typing import Tuple, List, Any


def render_sidebar_filters(
    devices: list = None,
    countries: list = None,
    show_top_n: bool = True,
    show_sort_by: bool = True,
    sort_options: list = None
) -> dict:
    """
    Renderiza filtros en el sidebar y retorna los valores seleccionados.
    
    Args:
        devices: Lista de dispositivos disponibles
        countries: Lista de países disponibles
        show_top_n: Si True, muestra slider de Top N
        show_sort_by: Si True, muestra selector de ordenamiento
        sort_options: Opciones para ordenar
        
    Returns:
        Dict con los valores de filtros seleccionados
    """
    st.sidebar.header("Filtros")
    
    filters = {}
    
    # Filtro de periodo
    filters['periodo'] = st.sidebar.date_input("Selecciona un periodo", [])
    
    # Filtro de país
    if countries is None:
        countries = ["Argentina", "México", "España", "Colombia"]
    filters['pais'] = st.sidebar.multiselect(
        "País",
        countries,
        default=countries[0] if countries else None
    )
    
    # Filtro de dispositivo
    if devices is not None:
        filters['dispositivo'] = st.sidebar.multiselect(
            "Dispositivo",
            devices,
            default=devices
        )
    
    # Top N slider
    if show_top_n:
        filters['top_n'] = st.sidebar.slider("Top N", 5, 50, 10)
    
    # Ordenar por
    if show_sort_by:
        if sort_options is None:
            sort_options = ['Usuarios', 'Intención de Registro', 'Registrados']
        filters['ordenar_por'] = st.sidebar.selectbox("Ordenar por", sort_options)
    
    return filters


def render_period_filter() -> list:
    """
    Renderiza solo el filtro de periodo.
    
    Returns:
        Lista de fechas seleccionadas
    """
    return st.sidebar.date_input("Selecciona un periodo", [])


def render_multiselect_filter(
    label: str,
    options: list,
    default: Any = None,
    key: str = None
) -> list:
    """
    Renderiza un filtro multiselect genérico.
    
    Args:
        label: Etiqueta del filtro
        options: Opciones disponibles
        default: Valor por defecto
        key: Key único para el widget
        
    Returns:
        Lista de valores seleccionados
    """
    if default is None:
        default = options
    return st.sidebar.multiselect(label, options, default=default, key=key)


def render_top_n_slider(
    label: str = "Top N",
    min_val: int = 5,
    max_val: int = 50,
    default: int = 10,
    key: str = None
) -> int:
    """
    Renderiza un slider para seleccionar Top N.
    
    Args:
        label: Etiqueta del slider
        min_val: Valor mínimo
        max_val: Valor máximo
        default: Valor por defecto
        key: Key único para el widget
        
    Returns:
        Valor seleccionado
    """
    return st.sidebar.slider(label, min_val, max_val, default, key=key)

