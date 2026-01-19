"""
Streamlit App - Entry Point
Configuración de navegación y páginas.
"""

import streamlit as st

# Configuración de la página (debe ir antes de cualquier otro comando st)
st.set_page_config(
    page_title="Infobae - Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define the pages desde el módulo pages/
main_page = st.Page("pages/main_page.py", title="Comportamiento & Conversión a Registro", icon="📊")
page_2 = st.Page("pages/page_2.py", title="Page 2", icon="❄️")
page_3 = st.Page("pages/page_3.py", title="Page 3", icon="🎉")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3])

# Run the selected page
pg.run()
