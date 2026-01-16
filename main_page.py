import streamlit as st

# Main page content
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Infobae - Comportamiento & Conversión", layout="wide")

st.title("📊 Comportamiento & Conversión a Registro")
st.markdown("---")

# --- 1. MOCK DE DATOS (Basado en tus reportes) ---
def load_mock_data():
    # Datos del Funnel
    funnel_data = {
        'Etapa': ['Usuarios Totales', 'Intención de Registro', 'Registro Finalizado'],
        'Cantidad': [35215, 3715, 615]
    }
    
    # Evolución Temporal (1 al 7 de Enero 2026)
    dates = pd.date_range(start="2026-01-01", end="2026-01-07")
    evolution_data = pd.DataFrame({
        'Fecha': dates,
        'Intención de Registro': [510, 780, 650, 720, 810, 1020, 1080], # Mock de sesiones
        'Registro': [45, 68, 95, 82, 195, 120, 360]
    })
    
    # Datos por Dispositivo
    device_data = pd.DataFrame({
        'Dispositivo': ['Mobile', 'Desktop', 'Tablet', 'Smart TV'],
        'Intención': [1450, 1380, 180, 100],
        'Registro': [380, 240, 20, 5]
    })

    return funnel_data, evolution_data, device_data

funnel, evolution, devices = load_mock_data()

# --- 2. FILTROS LATERALES ---
st.sidebar.header("Filtros")
periodo = st.sidebar.date_input("Selecciona un periodo", [])
pais = st.sidebar.multiselect("Pais", ["Argentina", "México", "España", "Colombia"], default="Argentina")
dispositivo = st.sidebar.multiselect("Dispositivo", devices['Dispositivo'].unique(), default=devices['Dispositivo'].unique())

# --- 3. KPIs PRINCIPALES ---
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Sesiones con Intención", "6.650") 
col2.metric("% Rebote", "4,7%", "-0.5%") 
col3.metric("Duración Media", "00:23:10") 
col4.metric("Interacción Media", "00:05:42") 
col5.metric("Tasa de Registro", "16,6%") 

st.markdown("---")

# --- 4. FUNNEL Y GRÁFICOS ---
left_col, right_col = st.columns([1, 1])

with left_col:
    st.subheader("🎯 Funnel de Registro")
    fig_funnel = go.Figure(go.Funnel(
        y = funnel['Etapa'],
        x = funnel['Cantidad'],
        textinfo = "value+percent initial",
        textposition = "inside",
        marker = {"color": ["#1565C0", "#2196F3", "#64B5F6"]},
        connector = {"line": {"color": "#4a4a4a", "width": 1}}
    ))
    fig_funnel.update_layout(
        height=400,
        margin=dict(t=20, b=20, l=20, r=20),
        funnelgap=0.1,  # Espaciado entre barras
        funnelgroupgap=0.1
    )
    st.plotly_chart(fig_funnel, use_container_width=True)
    st.info("**Recomendación:** Implementar medición de campos para identificar puntos de fricción.") 

with right_col:
    st.subheader("🎯 Funnel de Registro 2")
    valores_reales = funnel['Cantidad']
    etapas = funnel['Etapa']

    # Texto personalizado: "35,215,664 (100%)"
    textos = [f"{v:,}" for v in valores_reales]
    x_log = np.log10(valores_reales)

    fig_funnel2 = go.Figure(go.Funnel(
        y = etapas,
        x = x_log,
        text = textos,
        textinfo = "text+percent initial", # Muestra el valor real y % respecto al inicio
        textposition = "inside",
        insidetextanchor = "middle",
        marker = {
            # "color": ["#2450A6", "#1E43E6", "#1E88E6"],
            "color": ["#2450A6", "#1565C0", "#4E8ACF"],
            "line": {"width": 1, "color": "white"}
        },
        connector = {"fillcolor": "#A6C6ED", "line": {"width": 0}},
        hoverinfo = "y+text", # Al pasar el mouse muestra Etapa + Valor Real
    ))

    fig_funnel2.update_layout(
        title = {"text": "<b>Embudo de Conversión - Infobae</b><br><span style='font-size:12px'>Escala logarítmica aplicada para visibilidad</span>"},
        paper_bgcolor = "white",
        plot_bgcolor = "white",
        xaxis = {
            "showticklabels": False, # Escondemos los números del logaritmo (2, 4, 6, 8)
            "showgrid": False,
            "zeroline": False
        },
        margin = dict(l=200), # Espacio para que no se corten los nombres de las etapas
        height = 500
    )
    st.plotly_chart(fig_funnel2, use_container_width=True)
    st.info("**Recomendación:** Implementar medición de campos para identificar puntos de fricción.") 
    # st.subheader("📈 Evolución de Usuarios e Intención")
    # fig_evo = px.line(evolution, x='Fecha', y=['Intención de Registro', 'Registro'], 
    #               markers=True, line_shape="spline",
    #               color_discrete_map={"Intención de Registro": "#2196F3", "Registro": "#FF9800"})
    # st.plotly_chart(fig_evo, use_container_width=True)

# --- 5. CLASIFICACIÓN POR DISPOSITIVO ---
st.markdown("---")
st.subheader("📱 Clasificación Según Dispositivo") 
fig_device = px.bar(devices, x='Dispositivo', y=['Intención', 'Registro'], 
                    barmode='group', 
                    color_discrete_sequence=["#2196F3", "#FF9800"])
st.plotly_chart(fig_device, use_container_width=True)

# --- 6. TABLA DE FUENTE / MEDIO ---
st.subheader("🌐 Detalle por Fuente / Medio")
# Mock de la tabla de tu PDF
df_fuente = pd.DataFrame([
    {"Fuente/Medio": "(direct) / (none)", "Usuarios": 20795580, "Intención": 1507, "Registrados": 230},
    {"Fuente/Medio": "google / organic", "Usuarios": 9886000, "Intención": 1127, "Registrados": 192},
    {"Fuente/Medio": "bing / organic", "Usuarios": 164342, "Intención": 263, "Registrados": 37},
])
st.table(df_fuente)