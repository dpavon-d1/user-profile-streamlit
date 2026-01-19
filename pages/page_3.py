"""
Page 3 - Página de ejemplo
"""

import streamlit as st
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

from styles.css import get_all_css
from components.layout import render_header

# === CARGAR CSS GLOBAL ===
st.markdown(get_all_css(), unsafe_allow_html=True)

# === HEADER ===
render_header(
    title="Page 3 🎉",
    sidebar_text="Page 3 🎉"
)

# Contenido de la página
st.write("Esta es la página 3. Agregá tu contenido aquí.")

