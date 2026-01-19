import streamlit as st

# Main page content
# st.markdown("# Main page")
st.sidebar.markdown("# Main page")


import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Infobae - Comportamiento & Conversión", layout="wide")

# Logo centrado usando columnas vacías a los lados
_, col_center, _ = st.columns([2, 1, 2])
with col_center:
    st.image("icono.png", width=200, use_container_width=False)

st.markdown("<h1 style='text-align: center;'>Comportamiento & Conversión a Registro</h1>", unsafe_allow_html=True)
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

# --- 3. KPIs PRINCIPALES CON ESTILO CARD ---

# CSS para las cards y st.info
st.markdown("""
<style>
.metric-card {
    background-color: #ffffff;
    border-radius: 8px;
    padding: 10px 8px;
    box-shadow: 0 4px 4px rgba(0,0,0,0.1);
    border-left: 4px solid #F28322;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
}
.metric-card h3 {
    color: #666666;
    font-size: 14px;
    font-weight: 500;
    margin: 0 0 4px 0;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    text-align: center;
    width: 100%;
}
.metric-card p {
    color: #1a1a1a;
    font-size: 24px;
    font-weight: 700;
    margin: 0;
    line-height: 1;
    text-align: center;
    width: 100%;
}
/* Estilo para st.info - fondo transparente y texto negro */
div[data-testid="stAlert"] {
    background-color: transparent !important;
    border: none !important;
}
div[data-testid="stAlert"] > div {
    background-color: transparent !important;
}
div[data-testid="stAlert"] p {
    color: #000000 !important;
    font-size: 14px !important;
}
</style>
""", unsafe_allow_html=True)

# Cards con métricas originales
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>Sesiones con Intención</h3>
        <p>6.650</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>% Rebote</h3>
        <p>4,7%</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>Duración Media</h3>
        <p>00:23:10</p>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <h3>Interacción Media</h3>
        <p>00:05:42</p>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="metric-card">
        <h3>Tasa de Registro</h3>
        <p>16,6%</p>
    </div>
    """, unsafe_allow_html=True) 

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
    st.info("*Se recomienda implementar la medición de campos del formulario para identificar puntos de fricción y definir niveles de interés gradual según el progreso del usuario.*") 

with right_col:
    # === MAPA DE USUARIOS POR PAÍS ===
    st.subheader("Usuarios por País")
    # --- 5. Datos mock por país ---
    paises_data = pd.DataFrame({
        'Pais': ['Argentina', 'México', 'España', 'Colombia', 'Chile', 'Perú'],
        'ISO': ['ARG', 'MEX', 'ESP', 'COL', 'CHL', 'PER'],
        'Intención': [1507, 1127, 263, 450, 380, 290],
        'Registros': [2500, 1200, 680, 450, 380, 290]
    })

    # Mapa Choropleth (países coloreados por Registros)
    fig_mapa = px.choropleth(
        paises_data,
        locations='ISO',
        color='Registros',             # Colorear por Registros
        hover_name='Pais',
        hover_data=['Intención', 'Registros'],  # Mostrar ambas métricas en hover
        color_continuous_scale=[[0, '#F2C6A5'], [0.5, '#F28322'], [1, '#A64724']],
        projection='natural earth',
        title='Registros e Intención por País'
    )

    fig_mapa.update_layout(
        coloraxis_colorbar=dict(
            orientation="h",      # La barra ahora es horizontal
            thickness=15,         # Grosor de la barra
            title="Usuarios",    # Título de la escala
            yanchor="top",        # Anclamos la parte superior de la barra...
            y=-0.05,              # ...por debajo del eje del mapa (valores negativos bajan)
            xanchor="right",     # Centramos la barra...
            x=0.5,                # ...en el medio del gráfico
            len=0.5               # Longitud de la barra (50% del ancho del mapa)
        ),
        geo=dict(
            showframe=False,
            showcoastlines=False,       # Sin líneas de costa negras
            showland=True,
            landcolor='#f5f5f5',
            showcountries=True,
            countrycolor='#cccccc',     # Gris claro para bordes
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

    fig_mapa.update_traces(
    marker_line_color='#cccccc', # Igualamos al color de los otros países
    marker_line_width=0.5        # Le damos el mismo grosor
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
            'xanchor': 'center',
            'x': 0.5
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
    estados = ['Registrado', 'Con Intención']
    

    # Crear barras dinámicamente desde el DataFrame
    fig_sesion_historial = go.Figure()

    for i, row in df_sesion_historial.iterrows():
        fig_sesion_historial.add_trace(go.Bar(
            name=row['Tipo Usuario'],
            x=estados,
            y=[row['Registrado'], row['Con Intención']],
            marker_color=colores[i],
            width=0.25  # Barras más finas
        ))

    fig_sesion_historial.update_layout(
        barmode='group',
        title='Según historial de sesiones',
        bargap=0.5,
        bargroupgap=0.02,
        legend={
            'orientation': 'h',
            'yanchor': 'bottom',
            'y': 1.02,
            'xanchor': 'center',
            'x': 0.5
        },
        height=400  # Misma altura que los otros gráficos
    )


    st.plotly_chart(fig_sesion_historial, use_container_width=True)

with col_vacia2:
    # === TABLA CON MAPA DE CALOR ===

    # Datos de ejemplo (filas = categorías, columnas = métricas)
    df_heatmap_segmento_consumo = pd.DataFrame({
        'Segmento Consumo': ['0-5 Light', '6-10 Medium', '11-20 Heavy', '21+ Super Heavy'],
        # 'Usuarios Totales': [20795, 9886, 1643, 3200],
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




# === GRÁFICO COMBINADO (ambas métricas) ===

st.subheader("Evolución de Usuarios: Intención vs Registro")


fechas = pd.date_range(start="2026-01-01", end="2026-01-31")

fig_combinado = go.Figure()

df_evolucion = pd.DataFrame({
    'Fecha': fechas,
    'Intención de Registro': [510, 780, 650, 720, 810, 1020, 1080, 950, 890, 1150,
                              1230, 1100, 980, 1340, 1450, 1280, 1190, 1520, 1680, 1450,
                              1320, 1890, 2010, 1780, 1650, 2150, 2340, 2100, 1980, 2450, 2680],
    'Registro': [45, 68, 95, 82, 195, 120, 360, 280, 150, 320,
                 410, 380, 290, 520, 580, 450, 390, 620, 710, 550,
                 480, 780, 890, 720, 610, 920, 1050, 880, 750, 1120, 1280]
})

# Línea de Intención de Registro
fig_combinado.add_trace(go.Scatter(
    x=df_evolucion['Fecha'],
    y=df_evolucion['Intención de Registro'],
    mode='lines+markers',
    name='Intención',
    line=dict(color='#F28322', width=2),
    marker=dict(size=5)
))

# Línea de Registros
fig_combinado.add_trace(go.Scatter(
    x=df_evolucion['Fecha'],
    y=df_evolucion['Registro'],
    mode='lines+markers',
    name='Registros',
    line=dict(color='#2450A6', width=2),
    marker=dict(size=5)
))

fig_combinado.update_layout(
    title='📈 Evolución de Usuarios: Intención vs Registro',
    xaxis_title='Fecha',
    yaxis_title='Usuarios',
    height=450,
    hovermode='x unified',
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ),
    xaxis=dict(
        tickformat='%d/%m',
        dtick='D2',
        showgrid=False
    ),
     yaxis=dict(
        showgrid=True,
        gridcolor='#e0e0e0',
        gridwidth=1
    )
)

st.plotly_chart(fig_combinado, use_container_width=True)

st.subheader("Evolución de Sesiones: Intención vs Registro")

fig_combinado_sesiones = go.Figure()

df_evolucion_sesiones = pd.DataFrame({
    'Fecha': fechas,
    'Intención de Registro': [510, 780, 650, 720, 810, 1020, 1080, 950, 890, 1150,
                              1230, 1100, 980, 1340, 1450, 1280, 1190, 1520, 1680, 1450,
                              1320, 1890, 2010, 1780, 1650, 2150, 2340, 2100, 1980, 2450, 2680],
    'Registro': [45, 68, 95, 82, 195, 120, 360, 280, 150, 320,
                 410, 380, 290, 520, 580, 450, 390, 620, 710, 550,
                 480, 780, 890, 720, 610, 920, 1050, 880, 750, 1120, 1280]
})

# Línea de Intención de Registro
fig_combinado_sesiones.add_trace(go.Scatter(
    x=df_evolucion_sesiones['Fecha'],
    y=df_evolucion_sesiones['Intención de Registro'],
    mode='lines+markers',
    name='Intención de Registro',
    line=dict(color='#F28322', width=2),
    marker=dict(size=5)
))

# Línea de Registros
fig_combinado_sesiones.add_trace(go.Scatter(
    x=df_evolucion_sesiones['Fecha'],
    y=df_evolucion_sesiones['Registro'],
    mode='lines+markers',
    name='Registros',
    line=dict(color='#2450A6', width=2),
    marker=dict(size=5)
))

fig_combinado_sesiones.update_layout(
    title='📈 Evolución de Sesiones: Intención vs Registro',
    xaxis_title='Fecha',
    yaxis_title='Sesiones',
    height=450,
    hovermode='x unified',
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='right',
        x=1
    ),
    xaxis=dict(
        tickformat='%d/%m',
        dtick='D2',
        showgrid=False
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#e0e0e0',
        gridwidth=1
    )
)


st.plotly_chart(fig_combinado_sesiones, use_container_width=True)

st.subheader("Afinidad de Usuarios - Modelo Wattson")

# Datos por Concepto (20 conceptos para Top 15)
df_conceptos_all = pd.DataFrame({
    'Concepto': [
        'Inflación', 'Dólar', 'Elecciones', 'COVID-19', 'Jubilaciones',
        'Tarifas', 'Combustibles', 'Alquileres', 'Empleo', 'Impuestos',
        'Educación Pública', 'Salud Pública', 'Seguridad', 'Transporte', 'Clima',
        'Fútbol', 'Tenis', 'Cine', 'Música', 'Series'
    ],
    'Usuarios con Intención': [
        2450, 2180, 1950, 1720, 1580,
        1420, 1350, 1280, 1150, 1080,
        980, 920, 850, 780, 720,
        1890, 650, 580, 540, 490
    ],
    'Usuarios Registrados': [
        620, 540, 480, 410, 380,
        340, 320, 300, 280, 260,
        230, 210, 190, 170, 150,
        450, 130, 120, 110, 95
    ]
})

# Top 15 ordenado por Usuarios con Intención
df_conceptos = df_conceptos_all.nlargest(15, 'Usuarios con Intención')

# Colores para las métricas
color_intencion = '#2450A6'  # Naranja
color_registrados = '#F28322'  # Azul

# Crear gráfico de barras agrupadas
fig_barras_conceptos = go.Figure()

# Barras de Usuarios con Intención
fig_barras_conceptos.add_trace(go.Bar(
    name='Usuarios con Intención',
    x=df_conceptos['Concepto'],
    y=df_conceptos['Usuarios con Intención'],
    marker_color=color_intencion
))

# Barras de Usuarios Registrados
fig_barras_conceptos.add_trace(go.Bar(
    name='Usuarios Registrados',
    x=df_conceptos['Concepto'],
    y=df_conceptos['Usuarios Registrados'],
    marker_color=color_registrados
))

fig_barras_conceptos.update_layout(
    title='Top 15 Conceptos - Usuarios con Intención vs Registrados',
    xaxis_title='Concepto',
    yaxis_title='Usuarios',
    barmode='group',
    height=450,
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5
    ),
    xaxis=dict(
        showgrid=False,
        tickangle=-45  # Rotar etiquetas para mejor lectura
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#e0e0e0',
        gridwidth=1
    )
)

st.plotly_chart(fig_barras_conceptos, use_container_width=True)


# Datos por categoría Wattson (20 categorías para Top 15)
df_wattson_category_all = pd.DataFrame({
    'Categoría Wattson': [
        'Economía', 'Salud', 'Educación', 'Cultura', 'Deportes', 
        'Política', 'Ciencia', 'Tecnología', 'Entretenimiento', 'Sociedad',
        'Internacional', 'Nacional', 'Opinión', 'Lifestyle', 'Autos',
        'Turismo', 'Gastronomía', 'Moda', 'Celebridades', 'Gaming'
    ],
    'Usuarios con Intención': [
        1850, 1420, 980, 650, 2100, 
        1680, 350, 1280, 1560, 890,
        1720, 2340, 1150, 760, 480,
        540, 320, 410, 1050, 920
    ],
    'Usuarios Registrados': [
        420, 310, 180, 95, 520, 
        380, 50, 300, 360, 145,
        410, 580, 280, 190, 65,
        85, 45, 60, 260, 210
    ]
})

# Top 15 ordenado por Usuarios con Intención
df_wattson_category = df_wattson_category_all.nlargest(15, 'Usuarios con Intención')

# Colores para las métricas
color_intencion = '#2450A6'  # Azul 
color_registrados = '#F28322'  # Naranja

# Crear gráfico de barras agrupadas
fig_barras_wattson_category = go.Figure()

# Barras de Usuarios con Intención
fig_barras_wattson_category.add_trace(go.Bar(
    name='Usuarios con Intención',
    x=df_wattson_category['Categoría Wattson'],
    y=df_wattson_category['Usuarios con Intención'],
    marker_color=color_intencion
))

# Barras de Usuarios Registrados
fig_barras_wattson_category.add_trace(go.Bar(
    name='Usuarios Registrados',
    x=df_wattson_category['Categoría Wattson'],
    y=df_wattson_category['Usuarios Registrados'],
    marker_color=color_registrados
))

fig_barras_wattson_category.update_layout(
    title='Usuarios por Categoría Wattson',
    xaxis_title='Categoría',
    yaxis_title='Usuarios',
    barmode='group',
    height=450,
    plot_bgcolor='#ffffff',
    paper_bgcolor='#ffffff',
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5
    ),
    xaxis=dict(
        showgrid=False
    ),
    yaxis=dict(
        showgrid=True,
        gridcolor='#e0e0e0',
        gridwidth=1
    )
)

st.plotly_chart(fig_barras_wattson_category, use_container_width=True)


