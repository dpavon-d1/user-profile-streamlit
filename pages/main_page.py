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
from config import (
    CHART_CONFIG,
    COLORS,
    get_all_css,
    render_header,
    render_section_divider,
    render_section_title,
    render_info_box,
    render_chart_container,
    render_sidebar_filters
)
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
from charts import (
    create_funnel_chart,
    create_map,
    get_map_config,
    create_bar_chart,
    create_stacked_bar_chart,
    create_line_chart,
    create_heatmap_table,
    style_dataframe_heatmap,
    render_kpi_row
)

# === CARGAR CSS GLOBAL ===
st.markdown(get_all_css(), unsafe_allow_html=True)

# === HEADER ===
render_header(
    title="Comportamiento & Conversión a Registro",
    logo_path="pages/assets/icono.png",
    logo_width=200,
    sidebar_text="Comportamiento & Conversión a Registro"
)

# === LISTA DE DISPOSITIVOS Y PAÍSES DISPONIBLES ===
ALL_DEVICES = ['Mobile', 'Desktop', 'Tablet', 'Smart TV']
ALL_COUNTRIES = ["Argentina", "México", "España", "Colombia"]

# === FILTROS SIDEBAR ===
filters = render_sidebar_filters(
    devices=ALL_DEVICES,
    countries=ALL_COUNTRIES,
    show_top_n=False,
    show_sort_by=False
)

# Extraer valores de filtros
selected_countries = filters.get('pais', ALL_COUNTRIES)
selected_devices = filters.get('dispositivo', ALL_DEVICES)
selected_period = filters.get('periodo', [])


# Convertir periodo a tupla si tiene valores
date_range = tuple(selected_period) if len(selected_period) == 2 else None

# === CARGAR DATOS CON FILTROS ===
funnel_data = get_funnel_data(countries=selected_countries)
devices_df = get_device_data(devices=selected_devices)
kpi_data = get_kpi_data(countries=selected_countries)
country_data = get_country_data(countries=selected_countries)
evolution_df = get_evolution_data(date_range=date_range)

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
    
    # Mostrar mensaje si no hay países seleccionados
    if country_data.empty:
        st.warning("Selecciona al menos un país para ver el mapa.")
    else:
        fig_mapa = create_map(
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
    if devices_df.empty:
        st.warning("Selecciona al menos un dispositivo.")
    else:
        fig_device = create_bar_chart(
            df=devices_df,
            dimension_x_axis='Dispositivo',
            dimension_col='Registrado',
            breakdown_col='Con Intención',
            title='Según Dispositivo y Estado',
            height=CHART_CONFIG["bar_height"]
        )
        render_chart_container(fig_device)

with col_session:
    session_df = get_session_history_data()
    fig_session = create_bar_chart(
        df=session_df,
        dimension_x_axis='Tipo Usuario',
        dimension_col='Registrado',
        breakdown_col='Con Intención',
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
styled_df = style_dataframe_heatmap(source_df)

st.dataframe(styled_df, use_container_width=True, hide_index=True)

# === SECCIÓN: EVOLUCIÓN TEMPORAL ===
render_section_title("Evolución de Usuarios: Intención vs Registro")

if evolution_df.empty:
    st.warning("No hay datos para el periodo seleccionado.")
else:
    fig_evolution_users = create_line_chart(
        df=evolution_df,
        x_col='Fecha',
        y_cols=['Intención de Registro', 'Registro'],
        colors=[COLORS["primary"], COLORS["secondary"]],
        title='📈 Evolución de Usuarios: Intención vs Registro',
        y_title='Usuarios',
        date_format='%d/%m',
        dtick='D2'
    )
    render_chart_container(fig_evolution_users)

render_section_title("Evolución de Sesiones: Intención vs Registro")

if not evolution_df.empty:
    fig_evolution_sessions = create_line_chart(
        df=evolution_df,
        x_col='Fecha',
        y_cols=['Intención de Registro', 'Registro'],
        colors=[COLORS["primary"], COLORS["secondary"]],
        title='📈 Evolución de Sesiones: Intención vs Registro',
        y_title='Sesiones',
        date_format='%d/%m',
        dtick='D2'
    )
    render_chart_container(fig_evolution_sessions)

# === SECCIÓN: AFINIDAD WATTSON ===
render_section_title("Afinidad de Usuarios - Modelo Wattson")

# Conceptos
concepts_df = get_concepts_data()
concepts_df["totals"] = concepts_df["Usuarios con Intención"] + concepts_df["Usuarios Registrados"]
concepts_df = concepts_df.sort_values(by='totals', ascending=False)
concepts_df.drop(columns=['totals'], inplace=True)
fig_concepts = create_stacked_bar_chart(
    df=concepts_df,
    x_col='Concepto',
    y_cols=['Usuarios con Intención', 'Usuarios Registrados'],
    colors=[COLORS["secondary"], COLORS["primary"]],
    title='Conceptos - Usuarios con Intención vs Registrados',
    x_title='Concepto',
    y_title='Usuarios',
    rotate_labels=True,
    barmode='stack'
)
render_chart_container(fig_concepts)

# Categorías Wattson
categories_df = get_wattson_category_data()
categories_df["totals"] = categories_df["Usuarios con Intención"] + categories_df["Usuarios Registrados"]
categories_df = categories_df.sort_values(by='totals', ascending=False)
categories_df.drop(columns=['totals'], inplace=True)
fig_categories = create_stacked_bar_chart(
    df=categories_df,
    x_col='Categoría Wattson',
    y_cols=['Usuarios con Intención', 'Usuarios Registrados'],
    colors=[COLORS["secondary"], COLORS["primary"]],
    title='Usuarios por Categoría Wattson',
    x_title='Categoría',
    y_title='Usuarios',
    barmode='stack'
)
render_chart_container(fig_categories)
