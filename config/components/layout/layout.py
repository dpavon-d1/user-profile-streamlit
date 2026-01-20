"""
Layout components for Streamlit.
"""

import streamlit as st


def render_header(
    title: str,
    logo_path: str = None,
    logo_width: int = 200,
    sidebar_text: str = None
):
    """
    Render the page header with centered logo and title.
    
    Args:
        title: Main page title
        logo_path: Path to logo (optional)
        logo_width: Logo width in pixels
        sidebar_text: Text to show in sidebar (optional)
    """
    # Sidebar text
    if sidebar_text:
        st.sidebar.markdown(sidebar_text)
    
    # Centered logo
    if logo_path:
        _, col_center, _ = st.columns([2, 1, 2])
        with col_center:
            st.image(logo_path, width=logo_width, use_container_width=False)
    
    # Centered title
    st.markdown(
        f"<h1 style='text-align: center;'>{title}</h1>",
        unsafe_allow_html=True
    )
    
    # Divider line
    st.markdown("---")


def render_section_divider():
    """Render a divider line between sections."""
    st.markdown("---")


def render_section_title(title: str, emoji: str = None):
    """
    Render a section title.
    
    Args:
        title: Section title
        emoji: Optional emoji at the beginning
    """
    if emoji:
        st.subheader(f"{emoji} {title}")
    else:
        st.subheader(title)


def create_columns(ratios: list):
    """
    Create columns with specific proportions.
    
    Args:
        ratios: List of proportions (e.g.: [1, 1] for 50-50)
        
    Returns:
        Tuple of columns
    """
    return st.columns(ratios)


def render_info_box(text: str, italic: bool = True):
    """
    Render an information box.
    
    Args:
        text: Text to display
        italic: If True, displays in italic
    """
    if italic:
        st.info(f"*{text}*")
    else:
        st.info(text)


def render_chart_container(fig, use_container_width: bool = True, config: dict = None):
    """
    Render a Plotly chart with standard configuration.
    
    Args:
        fig: Plotly figure
        use_container_width: If True, uses full container width
        config: Additional chart configuration
    """
    if config is None:
        st.plotly_chart(fig, use_container_width=use_container_width)
    else:
        st.plotly_chart(fig, use_container_width=use_container_width, config=config)

