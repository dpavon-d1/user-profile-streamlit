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
    st.subheader("Funnel de Registro")
   
    valores= funnel['Cantidad']
    etapas = funnel['Etapa']

    # 2. Cálculos manuales
    # Porcentaje respecto al total (Paso 1)
    pct_initial = [(v / valores[0]) * 100 for v in valores]
    # Porcentaje respecto al paso anterior (opcional, muy útil)
    pct_previous = [100.0] + [(valores[i] / valores[i-1]) * 100 for i in range(1, len(valores))]

    # 3. Crear etiquetas de texto personalizadas
    # Formato: "35,215,664 (100%)"
    textos_personalizados = [
        f"{v:,}<br>{p:.2f}%" if p < 100 else f"{v:,}" 
        for v, p in zip(valores, pct_initial)
    ]


    fig_funnel = go.Figure(go.Funnel(
        y = etapas,
        x = np.log10(valores),
        text = textos_personalizados,
        textinfo = "text", 
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

    fig_funnel.update_layout(
        title = {"text": "<b>Embudo de Conversión - Infobae</b><br><span style='font-size:12px'>Escala logarítmica aplicada para visibilidad</span>"},
        # paper_bgcolor = "white",
        # plot_bgcolor = "white",
        xaxis = {
            "showticklabels": False, # Escondemos los números del logaritmo (2, 4, 6, 8)
            "showgrid": False,
            "zeroline": False
        },
        margin = dict(l=200), # Espacio para que no se corten los nombres de las etapas
        height = 500
    )


    st.plotly_chart(fig_funnel, use_container_width=True)
    st.info("**Recomendación:** Implementar medición de campos para identificar puntos de fricción.") 

with right_col:
    # === MAPA DE USUARIOS POR PAÍS ===
    st.subheader("Usuarios por País")
    # --- 5. Datos mock por país ---
    paises_data = pd.DataFrame({
        'Pais': ['Argentina', 'México', 'España', 'Colombia', 'Chile', 'Perú'],
        'ISO': ['ARG', 'MEX', 'ESP', 'COL', 'CHL', 'PER'],  # Códigos ISO para el mapa
        'Usuarios': [15000, 8500, 4200, 3100, 2800, 1900],
        'Registros': [2500, 1200, 680, 450, 380, 290]
    })

    # Mapa Choropleth (países coloreados por métrica)
    fig_mapa = px.choropleth(
        paises_data,
        locations='ISO',               # Columna con códigos de país
        color='Usuarios',              # Métrica para colorear
        hover_name='Pais',             # Nombre al pasar mouse
        hover_data=['Registros'],      # Datos adicionales en hover
        color_continuous_scale=[[0, '#4E8ACF'], [0.5, '#1565C0'], [1, '#2450A6']]  ,  # Escala de colores
        projection='natural earth',    # Tipo de proyección
    )

    fig_mapa.update_layout(
        geo=dict(
            showframe=False,
            showcoastlines=False,       # Sin líneas de costa
            showland=True,
            landcolor='#f5f5f5',
            showcountries=True,
            countrycolor='#cccccc',     # Gris claro para bordes de países
            countrywidth=0.5,           # Línea fina
            showlakes=False,
            showrivers=False,
            lataxis=dict(showgrid=False),
            lonaxis=dict(showgrid=False),
            showsubunits=False,
            framewidth=0
        ),
        height=500,
        margin=dict(l=0, r=0, t=50, b=0)
    )

    st.plotly_chart(fig_mapa, use_container_width=True, config={
        'scrollZoom': False,
        'doubleClick': False,
        'displayModeBar': False
    })

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