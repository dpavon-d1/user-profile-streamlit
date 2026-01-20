"""
Filter components for Streamlit sidebar.
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
    Render filters in the sidebar and return selected values.
    
    Args:
        devices: List of available devices
        countries: List of available countries
        show_top_n: If True, shows Top N slider
        show_sort_by: If True, shows sort selector
        sort_options: Options for sorting
        
    Returns:
        Dict with selected filter values
    """
    st.sidebar.header("Filtros")
    
    filters = {}
    
    # Period filter
    filters['periodo'] = st.sidebar.date_input("Selecciona un periodo", [])
    
    # Country filter
    if countries is None:
        countries = ["Argentina", "México", "España", "Colombia"]
    filters['pais'] = st.sidebar.multiselect(
        "País",
        countries,
        default=countries[0] if countries else None
    )
    
    # Device filter
    if devices is not None:
        filters['dispositivo'] = st.sidebar.multiselect(
            "Dispositivo",
            devices,
            default=devices
        )
    
    # Top N slider
    if show_top_n:
        filters['top_n'] = st.sidebar.slider("Top N", 5, 50, 10)
    
    # Sort by
    if show_sort_by:
        if sort_options is None:
            sort_options = ['Usuarios', 'Intención de Registro', 'Registrados']
        filters['ordenar_por'] = st.sidebar.selectbox("Ordenar por", sort_options)
    
    return filters


def render_period_filter() -> list:
    """
    Render only the period filter.
    
    Returns:
        List of selected dates
    """
    return st.sidebar.date_input("Selecciona un periodo", [])


def render_multiselect_filter(
    label: str,
    options: list,
    default: Any = None,
    key: str = None
) -> list:
    """
    Render a generic multiselect filter.
    
    Args:
        label: Filter label
        options: Available options
        default: Default value
        key: Unique key for the widget
        
    Returns:
        List of selected values
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
    Render a slider to select Top N.
    
    Args:
        label: Slider label
        min_val: Minimum value
        max_val: Maximum value
        default: Default value
        key: Unique key for the widget
        
    Returns:
        Selected value
    """
    return st.sidebar.slider(label, min_val, max_val, default, key=key)

