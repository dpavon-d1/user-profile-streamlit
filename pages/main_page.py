"""
Main Page - Dashboard de Comportamiento & Conversión a Registro
Versión modularizada para escalabilidad y reutilización.
"""

import streamlit as st
import sys
from pathlib import Path

# Agregar el directorio raíz al path para imports
ROOT_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT_DIR))

# === IMPORTS DE MÓDULOS PROPIOS ===
from config.settings import PAGE_CONFIG, CHART_CONFIG, MAP_CONFIG, TOP_N_CONFIG
from styles.css import get_all_css
from styles.colors import COLORS
from data.mock_data import (
    get_funnel_data,
    get_evolution_data,
    get_device_data,
    get_session_history_data,
    get_country_data,
    get_segment_data,
    get_source_medium_data,
    get_concepts_data,
    get_wattson_category_data,
    get_kpi_data
)
from charts.funnel import create_funnel_chart
from charts.maps import create_choropleth_map, get_map_config
from charts.bar_charts import (
    create_device_bar_chart,
    create_session_history_chart,
    create_grouped_bar_chart
)
from charts.line_charts import create_evolution_chart
from charts.heatmaps import create_heatmap_table, style_dataframe_heatmap, filter_top_n
from components.layout import (
    render_header,
    render_section_divider,
    render_section_title,
    render_info_box,
    render_chart_container
)
from components.kpi_cards import render_kpi_row
from components.filters import render_sidebar_filters

# === CARGAR CSS GLOBAL ===
st.markdown(get_all_css(), unsafe_allow_html=True)

# === HEADER ===
render_header(
    title="Comportamiento & Conversión a Registro",
    logo_path="icono.png",
    logo_width=200,
    sidebar_text="Comportamiento & Conversión a Registro"
)

# === CARGAR DATOS ===
funnel_data = get_funnel_data()
devices_df = get_device_data()
kpi_data = get_kpi_data()

# === FILTROS SIDEBAR ===
filters = render_sidebar_filters(
    devices=devices_df['Dispositivo'].tolist(),
    countries=["Argentina", "México", "España", "Colombia"],
    show_top_n=True,
    show_sort_by=True
)

# === KPIs PRINCIPALES ===
render_kpi_row(kpi_data)

render_section_divider()

# === SECCIÓN: FUNNEL Y MAPA ===
left_col, right_col = st.columns([1, 1])

with left_col:
    render_section_title("Funnel de Registro")
    
    fig_funnel = create_funnel_chart(
        etapas=funnel_data['Etapa'],
        valores=funnel_data['Cantidad'],
        title="Embudo de Conversión - Infobae",
        subtitle="Escala logarítmica aplicada para visibilidad",
        height=CHART_CONFIG["funnel_height"]
    )
    
    render_chart_container(fig_funnel)
    render_info_box(
        "Se recomienda implementar la medición de campos del formulario para "
        "identificar puntos de fricción y definir niveles de interés gradual "
        "según el progreso del usuario."
    )

with right_col:
    render_section_title("Usuarios por País")
    
    country_data = get_country_data()
    fig_mapa = create_choropleth_map(
        df=country_data,
        locations_col='ISO',
        color_col='Registros',
        hover_name_col='Pais',
        hover_data_cols=['Intención', 'Registros'],
        title='Registros e Intención por País',
        height=CHART_CONFIG["map_height"]
    )
    
    render_chart_container(fig_mapa, config=get_map_config())

# === SECCIÓN: CLASIFICACIÓN DE USUARIOS ===
render_section_divider()
render_section_title("Clasificación de Usuarios")

col_device, col_session, col_segment = st.columns([1, 1, 1])

with col_device:
    fig_device = create_device_bar_chart(
        df=devices_df,
        title='Según Dispositivo y Estado',
        height=CHART_CONFIG["bar_height"]
    )
    render_chart_container(fig_device)

with col_session:
    session_df = get_session_history_data()
    fig_session = create_session_history_chart(
        df=session_df,
        title='Según historial de sesiones',
        height=CHART_CONFIG["bar_height"]
    )
    render_chart_container(fig_session)

with col_segment:
    segment_df = get_segment_data()
    fig_segment = create_heatmap_table(
        df=segment_df,
        index_col='Segmento Consumo',
        title='Según segmento consumo',
        height=CHART_CONFIG["heatmap_height"],
        show_colorbar=False
    )
    render_chart_container(fig_segment)

# === SECCIÓN: TABLA FUENTE/MEDIO ===
render_section_title("Detalle por Fuente / Medio")

source_df = get_source_medium_data()
df_filtered = filter_top_n(source_df, filters['top_n'], filters['ordenar_por'])
styled_df = style_dataframe_heatmap(df_filtered)

st.dataframe(styled_df, use_container_width=True, hide_index=True)

# === SECCIÓN: EVOLUCIÓN TEMPORAL ===
render_section_title("Evolución de Usuarios: Intención vs Registro")

evolution_df = get_evolution_data()
fig_evolution_users = create_evolution_chart(
    df=evolution_df,
    metrics=['Intención de Registro', 'Registro'],
    colors=[COLORS["primary"], COLORS["secondary"]],
    title='Evolución de Usuarios: Intención vs Registro',
    y_title='Usuarios'
)
render_chart_container(fig_evolution_users)

render_section_title("Evolución de Sesiones: Intención vs Registro")

fig_evolution_sessions = create_evolution_chart(
    df=evolution_df,
    metrics=['Intención de Registro', 'Registro'],
    colors=[COLORS["primary"], COLORS["secondary"]],
    title='Evolución de Sesiones: Intención vs Registro',
    y_title='Sesiones'
)
render_chart_container(fig_evolution_sessions)

# === SECCIÓN: AFINIDAD WATTSON ===
render_section_title("Afinidad de Usuarios - Modelo Wattson")

# Top 15 Conceptos
concepts_df = get_concepts_data(top_n=TOP_N_CONFIG["conceptos"])
fig_concepts = create_grouped_bar_chart(
    df=concepts_df,
    x_col='Concepto',
    y_cols=['Usuarios con Intención', 'Usuarios Registrados'],
    colors=[COLORS["secondary"], COLORS["primary"]],
    title='Top 15 Conceptos - Usuarios con Intención vs Registrados',
    x_title='Concepto',
    y_title='Usuarios',
    rotate_labels=True
)
render_chart_container(fig_concepts)

# Top 15 Categorías Wattson
categories_df = get_wattson_category_data(top_n=TOP_N_CONFIG["categorias"])
fig_categories = create_grouped_bar_chart(
    df=categories_df,
    x_col='Categoría Wattson',
    y_cols=['Usuarios con Intención', 'Usuarios Registrados'],
    colors=[COLORS["secondary"], COLORS["primary"]],
    title='Usuarios por Categoría Wattson',
    x_title='Categoría',
    y_title='Usuarios'
)
render_chart_container(fig_categories)

