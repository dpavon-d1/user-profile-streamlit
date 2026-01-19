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
st.subheader("Clasificación de Usuarios") 

# Columnas: gráfico a la izquierda (60%), espacio vacío a la derecha (40%)
col_grafico, col_vacia, col_vacia2 = st.columns([1, 1, 1])

with col_grafico:
    df_dispositivos = pd.DataFrame({
        'Dispositivo': ['Mobile', 'Desktop', 'Tablet', 'Smart TV'],
        'Registrado': [20, 12, 12, 12],
        'Con Intención': [14, 38, 28, 88]
    })

    # Colores por dispositivo
    colores = ['#A64724', '#F28322', 'rgb(51,153,255)', '#2450A6']
    estados = ['Registrado', 'Con Intención']

    # Crear barras dinámicamente desde el DataFrame
    fig_device = go.Figure()

    for i, row in df_dispositivos.iterrows():
        fig_device.add_trace(go.Bar(
            name=row['Dispositivo'],
            x=estados,
            y=[row['Registrado'], row['Con Intención']],
            marker_color=colores[i]
        ))

    fig_device.update_layout(
        barmode='group',
        title='Según Dispositivo y Estado',
        # yaxis={'title': {'text': 'Usuarios'}},
        # xaxis={'title': {'text': 'Estado Usuario'}},
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        height=400
    )
    st.plotly_chart(fig_device, use_container_width=True)

with col_vacia:
    df_sesion_historial = pd.DataFrame({
    'Tipo Usuario': ['Recurrente', 'Nuevo'],
    'Registrado': [20,56],
    'Con Intención': [14,89]
    })

    # Colores por dispositivo
    colores = ['#A64724', '#F28322', 'rgb(51,153,255)', '#2450A6']
    estados = ['Recurrente', 'Nuevo']

    # Crear barras dinámicamente desde el DataFrame
    fig_sesion_historial = go.Figure()

    for i, row in df_sesion_historial.iterrows():
        fig_sesion_historial.add_trace(go.Bar(
            name=row['Tipo Usuario'],
            x=estados,
            y=[row['Registrado'], row['Con Intención']],
            marker_color=colores[i]
        ))

    fig_sesion_historial.update_layout(
        barmode='group',
        title='Según historial de sesiones',
        # yaxis={'title': {'text': 'Usuarios'}},
        # xaxis={'title': {'text': 'Tipo Usuario'}},
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'right',
            'x': 1
        },
        height=400
    )

    st.plotly_chart(fig_sesion_historial, use_container_width=True)

with col_vacia2:
    # === TABLA CON MAPA DE CALOR ===

    # Datos de ejemplo (filas = categorías, columnas = métricas)
    df_heatmap_segmento_consumo = pd.DataFrame({
        'Segmento Consumo': ['0-5 Light', '6-10 Medium', '11-20 Heavy', '21+ Super Heavy'],
        'Usuarios Totales': [20795, 9886, 1643, 3200],
        'Intención': [1507, 1127, 263, 450],
        'Registrados': [230, 192, 37, 85],
        # 'Tasa Conv %': [1.1, 1.9, 2.3, 2.7]
    })

    # Establecer la columna Segmento Consumo como índice
    df_heatmap_segmento_consumo = df_heatmap_segmento_consumo.set_index('Segmento Consumo')

    # OPCIÓN 1: Heatmap con Plotly (gráfico interactivo)
    fig_heatmap_segmento_consumo = go.Figure(data=go.Heatmap(
        showscale=False,
        z=df_heatmap_segmento_consumo.values,
        x=df_heatmap_segmento_consumo.columns,
        y=df_heatmap_segmento_consumo.index,
        colorscale=[[0, '#FEF0E3'], [0.5, '#F9B86C'], [1, '#F28322']],  # Escala naranja
        text=df_heatmap_segmento_consumo.values,
        texttemplate='%{text:,.0f}',
        textfont={'size': 12},
        hovertemplate='Fuente: %{y}<br>Métrica: %{x}<br>Valor: %{z:,.0f}<extra></extra>'
    ))

    fig_heatmap_segmento_consumo.update_layout(
        title='Según segmento consumo',
        height=400,
        # xaxis={'title': 'Usuarios'},
        # yaxis={'title': 'Segmento Consumo', 'autorange': 'reversed'}  # Para que la primera fila quede arriba
    )

    st.plotly_chart(fig_heatmap_segmento_consumo, use_container_width=True)

# --- 6. TABLA DE FUENTE / MEDIO ---
st.subheader("Detalle por Fuente / Medio")

from matplotlib.colors import LinearSegmentedColormap

# Datos de ejemplo con más fuentes/medios
df_custom = pd.DataFrame({
    'Fuente / Medio': [
        '(direct) / (none)',
        'google / organic',
        'google / cpc',
        'bing / organic',
        'bing / cpc',
        'yahoo / organic',
        'duckduckgo / organic',
        'facebook.com / referral',
        'instagram.com / referral',
        'twitter.com / referral',
        'linkedin.com / referral',
        'tiktok.com / referral',
        'youtube.com / referral',
        'news.google.com / referral',
        'flipboard.com / referral',
        'pinterest.com / referral',
        'reddit.com / referral',
        'whatsapp / referral',
        'telegram / referral',
        'email / newsletter',
        'email / marketing',
        'email / transactional',
        'push / notification',
        'app / internal',
        'ampproject.org / referral'
    ],
    'Usuarios': [
        20795580, 9886000, 1061458, 164342, 45230, 28450, 12300,
        851689, 456780, 234560, 189340, 567890, 345670,
        510695, 123450, 98760, 156780, 234560, 89450,
        321168, 156780, 45670, 234560, 678900, 756168
    ],
    'Intención de Registro': [
        1507, 1127, 322, 263, 89, 45, 23,
        83, 156, 78, 234, 345, 123,
        21, 34, 12, 67, 89, 23,
        456, 234, 67, 123, 45, 88
    ],
    'Registrados': [
        230, 192, 62, 37, 12, 8, 4,
        5, 23, 11, 45, 67, 19,
        4, 5, 2, 12, 15, 4,
        89, 45, 12, 23, 8, 8
    ]
})

# Crear escalas de color personalizadas (de claro a oscuro)
cmap_naranja = LinearSegmentedColormap.from_list('naranja', ['#FEF0E3', '#E38766', '#A64724'])
cmap_azul = LinearSegmentedColormap.from_list('azul', ['#E3F0FE', '#4E8ACF', '#2450A6'])
cmap_purpura = LinearSegmentedColormap.from_list('purpura', ['#FFF1E5', '#F5A964', '#F28322'])

# Aplicar colores personalizados
styled_custom = df_custom.style.background_gradient(
    subset=['Usuarios'], 
    cmap=cmap_azul
).background_gradient(
    subset=['Intención de Registro'], 
    cmap=cmap_naranja
).background_gradient(
    subset=['Registrados'], 
    cmap=cmap_purpura
).format({
    'Usuarios': '{:,.0f}',
    'Intención de Registro': '{:,.0f}',
    'Registrados': '{:,.0f}'
})

# Selectores en sidebar
top_n = st.sidebar.slider("Top N", 5, 50, 10)
ordenar_por = st.sidebar.selectbox("Ordenar por", ['Usuarios', 'Intención de Registro', 'Registrados'])

# Filtrar
df_top = df_custom.nlargest(top_n, ordenar_por)

# Mostrar
st.dataframe(styled_custom, use_container_width=True, hide_index=True)