"""
Datos mock para el dashboard.
En producción, estas funciones se reemplazarían por consultas a base de datos o APIs.
"""

import pandas as pd


# ============================================================
# FUNNEL DE CONVERSIÓN
# ============================================================

def get_funnel_data() -> dict:
    """
    Retorna datos del funnel de conversión.
    
    Returns:
        dict con 'Etapa' y 'Cantidad'
    """
    return {
        'Etapa': ['Usuarios Totales', 'Intención de Registro', 'Registro Finalizado'],
        'Cantidad': [35215, 3715, 615]
    }


# ============================================================
# EVOLUCIÓN TEMPORAL
# ============================================================

def get_evolution_data(start_date: str = "2026-01-01", end_date: str = "2026-01-31") -> pd.DataFrame:
    """
    Retorna datos de evolución temporal de usuarios.
    
    Args:
        start_date: Fecha de inicio
        end_date: Fecha de fin
        
    Returns:
        DataFrame con Fecha, Intención de Registro, Registro
    """
    fechas = pd.date_range(start=start_date, end=end_date)
    
    # Datos mock - en producción esto vendría de una query
    intencion = [510, 780, 650, 720, 810, 1020, 1080, 950, 890, 1150,
                 1230, 1100, 980, 1340, 1450, 1280, 1190, 1520, 1680, 1450,
                 1320, 1890, 2010, 1780, 1650, 2150, 2340, 2100, 1980, 2450, 2680]
    
    registro = [45, 68, 95, 82, 195, 120, 360, 280, 150, 320,
                410, 380, 290, 520, 580, 450, 390, 620, 710, 550,
                480, 780, 890, 720, 610, 920, 1050, 880, 750, 1120, 1280]
    
    return pd.DataFrame({
        'Fecha': fechas[:len(intencion)],
        'Intención de Registro': intencion,
        'Registro': registro
    })


# ============================================================
# DATOS POR DISPOSITIVO
# ============================================================

def get_device_data() -> pd.DataFrame:
    """
    Retorna datos de usuarios por dispositivo.
    
    Returns:
        DataFrame con Dispositivo, Registrado, Con Intención
    """
    return pd.DataFrame({
        'Dispositivo': ['Mobile', 'Desktop', 'Tablet', 'Smart TV'],
        'Registrado': [20, 12, 12, 12],
        'Con Intención': [14, 38, 28, 88]
    })


# ============================================================
# DATOS POR HISTORIAL DE SESIÓN
# ============================================================

def get_session_history_data() -> pd.DataFrame:
    """
    Retorna datos por tipo de usuario (nuevo vs recurrente).
    
    Returns:
        DataFrame con Tipo Usuario, Registrado, Con Intención
    """
    return pd.DataFrame({
        'Tipo Usuario': ['Recurrente', 'Nuevo'],
        'Registrado': [20, 56],
        'Con Intención': [14, 89]
    })


# ============================================================
# DATOS POR PAÍS
# ============================================================

def get_country_data() -> pd.DataFrame:
    """
    Retorna datos de usuarios por país.
    
    Returns:
        DataFrame con Pais, ISO, Intención, Registros
    """
    return pd.DataFrame({
        'Pais': ['Argentina', 'México', 'España', 'Colombia', 'Chile', 'Perú'],
        'ISO': ['ARG', 'MEX', 'ESP', 'COL', 'CHL', 'PER'],
        'Intención': [1507, 1127, 263, 450, 380, 290],
        'Registros': [2500, 1200, 680, 450, 380, 290]
    })


# ============================================================
# DATOS POR SEGMENTO DE CONSUMO
# ============================================================

def get_segment_data() -> pd.DataFrame:
    """
    Retorna datos por segmento de consumo.
    
    Returns:
        DataFrame con Segmento Consumo, Intención, Registrados
    """
    return pd.DataFrame({
        'Segmento Consumo': ['0-5 Light', '6-10 Medium', '11-20 Heavy', '21+ Super Heavy'],
        'Intención': [1507, 1127, 263, 450],
        'Registrados': [230, 192, 37, 85]
    })


# ============================================================
# DATOS POR FUENTE / MEDIO
# ============================================================

def get_source_medium_data() -> pd.DataFrame:
    """
    Retorna datos por fuente/medio de tráfico.
    
    Returns:
        DataFrame con Fuente / Medio, Usuarios, Intención de Registro, Registrados
    """
    return pd.DataFrame({
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


# ============================================================
# DATOS POR CONCEPTO (WATTSON)
# ============================================================

def get_concepts_data(top_n: int = 15) -> pd.DataFrame:
    """
    Retorna datos por concepto del modelo Wattson.
    
    Args:
        top_n: Número de conceptos top a retornar
        
    Returns:
        DataFrame con Concepto, Usuarios con Intención, Usuarios Registrados
    """
    df_all = pd.DataFrame({
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
    
    return df_all.nlargest(top_n, 'Usuarios con Intención')


# ============================================================
# DATOS POR CATEGORÍA WATTSON
# ============================================================

def get_wattson_category_data(top_n: int = 15) -> pd.DataFrame:
    """
    Retorna datos por categoría del modelo Wattson.
    
    Args:
        top_n: Número de categorías top a retornar
        
    Returns:
        DataFrame con Categoría Wattson, Usuarios con Intención, Usuarios Registrados
    """
    df_all = pd.DataFrame({
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
    
    return df_all.nlargest(top_n, 'Usuarios con Intención')


# ============================================================
# DATOS DE KPIs
# ============================================================

def get_kpi_data() -> dict:
    """
    Retorna datos de KPIs principales.
    
    Returns:
        dict con los KPIs del dashboard
    """
    return {
        'sesiones_intencion': '6.650',
        'pct_rebote': '4,7%',
        'duracion_media': '00:23:10',
        'interaccion_media': '00:05:42',
        'tasa_registro': '16,6%'
    }

