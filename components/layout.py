"""
Componentes de layout para Streamlit.
"""

import streamlit as st


def render_header(
    title: str,
    logo_path: str = None,
    logo_width: int = 200,
    sidebar_text: str = None
):
    """
    Renderiza el header de la página con logo y título centrados.
    
    Args:
        title: Título principal de la página
        logo_path: Ruta al logo (opcional)
        logo_width: Ancho del logo en pixels
        sidebar_text: Texto para mostrar en sidebar (opcional)
    """
    # Texto en sidebar
    if sidebar_text:
        st.sidebar.markdown(sidebar_text)
    
    # Logo centrado
    if logo_path:
        _, col_center, _ = st.columns([2, 1, 2])
        with col_center:
            st.image(logo_path, width=logo_width, use_container_width=False)
    
    # Título centrado
    st.markdown(
        f"<h1 style='text-align: center;'>{title}</h1>",
        unsafe_allow_html=True
    )
    
    # Línea divisoria
    st.markdown("---")


def render_section_divider():
    """Renderiza una línea divisoria entre secciones."""
    st.markdown("---")


def render_section_title(title: str, emoji: str = None):
    """
    Renderiza un título de sección.
    
    Args:
        title: Título de la sección
        emoji: Emoji opcional al inicio
    """
    if emoji:
        st.subheader(f"{emoji} {title}")
    else:
        st.subheader(title)


def create_columns(ratios: list):
    """
    Crea columnas con proporciones específicas.
    
    Args:
        ratios: Lista de proporciones (ej: [1, 1] para 50-50)
        
    Returns:
        Tupla de columnas
    """
    return st.columns(ratios)


def render_info_box(text: str, italic: bool = True):
    """
    Renderiza un cuadro de información.
    
    Args:
        text: Texto a mostrar
        italic: Si True, muestra en itálica
    """
    if italic:
        st.info(f"*{text}*")
    else:
        st.info(text)


def render_chart_container(fig, use_container_width: bool = True, config: dict = None):
    """
    Renderiza un gráfico de Plotly con configuración estándar.
    
    Args:
        fig: Figura de Plotly
        use_container_width: Si True, usa el ancho completo del contenedor
        config: Configuración adicional para el gráfico
    """
    if config is None:
        st.plotly_chart(fig, use_container_width=use_container_width)
    else:
        st.plotly_chart(fig, use_container_width=use_container_width, config=config)

