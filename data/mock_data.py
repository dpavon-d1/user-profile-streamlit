"""
Mock data for the dashboard.
In production, these functions would be replaced with database queries or APIs.
"""

import pandas as pd
from typing import List, Optional
from datetime import date


# ============================================================
# FILTERING FUNCTIONS
# ============================================================

def filter_by_country(df: pd.DataFrame, countries: List[str], country_col: str = 'Pais') -> pd.DataFrame:
    """
    Filter a DataFrame by selected countries.
    
    Args:
        df: DataFrame to filter
        countries: List of countries to include
        country_col: Country column name
        
    Returns:
        Filtered DataFrame
    """
    if not countries or country_col not in df.columns:
        return df
    return df[df[country_col].isin(countries)]


def filter_by_device(df: pd.DataFrame, devices: List[str], device_col: str = 'Dispositivo') -> pd.DataFrame:
    """
    Filter a DataFrame by selected devices.
    
    Args:
        df: DataFrame to filter
        devices: List of devices to include
        device_col: Device column name
        
    Returns:
        Filtered DataFrame
    """
    if not devices or device_col not in df.columns:
        return df
    return df[df[device_col].isin(devices)]


def filter_by_date_range(df: pd.DataFrame, start_date: date, end_date: date, date_col: str = 'Fecha') -> pd.DataFrame:
    """
    Filter a DataFrame by date range.
    
    Args:
        df: DataFrame to filter
        start_date: Start date
        end_date: End date
        date_col: Date column name
        
    Returns:
        Filtered DataFrame
    """
    if date_col not in df.columns:
        return df
    
    df_copy = df.copy()
    df_copy[date_col] = pd.to_datetime(df_copy[date_col])
    
    return df_copy[(df_copy[date_col].dt.date >= start_date) & (df_copy[date_col].dt.date <= end_date)]


def filter_top_n(df: pd.DataFrame, n: int, column: str) -> pd.DataFrame:
    """
    Filter top N records from a DataFrame.
    
    Args:
        df: DataFrame to filter
        n: Number of records
        column: Column to sort by
        
    Returns:
        Filtered DataFrame
    """
    if column not in df.columns:
        return df.head(n)
    return df.nlargest(n, column)


# ============================================================
# CONVERSION FUNNEL
# ============================================================

def get_funnel_data(countries: List[str] = None) -> dict:
    """
    Return conversion funnel data.
    
    Args:
        countries: List of countries to filter (mock: adjusts values proportionally)
    
    Returns:
        dict with 'Etapa' and 'Cantidad'
    """
    # Base data
    base_data = {
        'Etapa': ['Usuarios Totales', 'Intención de Registro', 'Registro Finalizado'],
        'Cantidad': [35215, 3715, 615]
    }
    
    # Mock: adjust based on number of selected countries
    if countries:
        all_countries = ["Argentina", "México", "España", "Colombia"]
        ratio = len(countries) / len(all_countries)
        base_data['Cantidad'] = [int(v * ratio) for v in base_data['Cantidad']]
    
    return base_data


# ============================================================
# TEMPORAL EVOLUTION
# ============================================================

def get_evolution_data(
    start_date: str = "2026-01-01", 
    end_date: str = "2026-01-31",
    date_range: tuple = None
) -> pd.DataFrame:
    """
    Return temporal evolution data for users.
    
    Args:
        start_date: Default start date
        end_date: Default end date
        date_range: Tuple of (start_date, end_date) from filter
        
    Returns:
        DataFrame with Fecha, Intención de Registro, Registro
    """
    fechas = pd.date_range(start=start_date, end=end_date)
    
    # Mock data
    intencion = [510, 780, 650, 720, 810, 1020, 1080, 950, 890, 1150,
                 1230, 1100, 980, 1340, 1450, 1280, 1190, 1520, 1680, 1450,
                 1320, 1890, 2010, 1780, 1650, 2150, 2340, 2100, 1980, 2450, 2680]
    
    registro = [45, 68, 95, 82, 195, 120, 360, 280, 150, 320,
                410, 380, 290, 520, 580, 450, 390, 620, 710, 550,
                480, 780, 890, 720, 610, 920, 1050, 880, 750, 1120, 1280]
    
    df = pd.DataFrame({
        'Fecha': fechas[:len(intencion)],
        'Intención de Registro': intencion,
        'Registro': registro
    })
    
    # Apply date filter if exists
    if date_range and len(date_range) == 2:
        df = filter_by_date_range(df, date_range[0], date_range[1])
    
    return df


# ============================================================
# DEVICE DATA
# ============================================================

def get_device_data(devices: List[str] = None) -> pd.DataFrame:
    """
    Return user data by device.
    
    Args:
        devices: List of devices to filter
    
    Returns:
        DataFrame with Dispositivo, Registrado, Con Intención
    """
    df = pd.DataFrame({
        'Dispositivo': ['Mobile', 'Desktop', 'Tablet', 'Smart TV'],
        'Registrado': [20, 12, 12, 8],
        'Con Intención': [14, 38, 28, 8]
    })
    
    return filter_by_device(df, devices) if devices else df


# ============================================================
# SESSION HISTORY DATA
# ============================================================

def get_session_history_data() -> pd.DataFrame:
    """
    Return data by user type (new vs returning).
    
    Returns:
        DataFrame with Tipo Usuario, Registrado, Con Intención
    """
    return pd.DataFrame({
        'Tipo Usuario': ['Recurrente', 'Nuevo'],
        'Registrado': [20, 56],
        'Con Intención': [14, 89]
    })


# ============================================================
# COUNTRY DATA
# ============================================================

def get_country_data(countries: List[str] = None) -> pd.DataFrame:
    """
    Return user data by country.
    
    Args:
        countries: List of countries to filter
    
    Returns:
        DataFrame with Pais, ISO, Intención, Registros
    """
    df = pd.DataFrame({
        'Pais': ['Argentina', 'México', 'España', 'Colombia', 'Chile', 'Perú'],
        'ISO': ['ARG', 'MEX', 'ESP', 'COL', 'CHL', 'PER'],
        'Intención': [1507, 1127, 263, 450, 380, 290],
        'Registros': [2500, 1200, 680, 450, 380, 290]
    })
    
    return filter_by_country(df, countries) if countries else df


# ============================================================
# CONSUMPTION SEGMENT DATA
# ============================================================

def get_segment_data() -> pd.DataFrame:
    """
    Return data by consumption segment.
    
    Returns:
        DataFrame with Segmento Consumo, Intención, Registrados
    """
    return pd.DataFrame({
        'Segmento Consumo': ['0-5 Light', '6-10 Medium', '11-20 Heavy', '21+ Super Heavy'],
        'Intención': [1507, 1127, 263, 450],
        'Registrados': [230, 192, 37, 85]
    })


# ============================================================
# SOURCE / MEDIUM DATA
# ============================================================

def get_source_medium_data() -> pd.DataFrame:
    """
    Return data by traffic source/medium.
    
    Returns:
        DataFrame with Fuente / Medio, Usuarios, Intención de Registro, Registrados
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
# CONCEPT DATA (WATTSON)
# ============================================================

def get_concepts_data() -> pd.DataFrame:
    """
    Return data by Wattson model concept.
        
    Returns:
        DataFrame with Concepto, Usuarios con Intención, Usuarios Registrados
    """
    return pd.DataFrame({
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

    


# ============================================================
# WATTSON CATEGORY DATA
# ============================================================

def get_wattson_category_data() -> pd.DataFrame:
    """
    Return data by Wattson model category.
        
    Returns:
        DataFrame with Categoría Wattson, Usuarios con Intención, Usuarios Registrados
    """
    return pd.DataFrame({
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


# ============================================================
# KPI DATA
# ============================================================

def get_kpi_data(countries: List[str] = None) -> dict:
    """
    Return main KPI data.
    
    Args:
        countries: List of countries (mock: adjusts values)
    
    Returns:
        dict with dashboard KPIs
    """

    # Base values
    kpis = {
        'sesiones_intencion': 6650,
        'pct_rebote': 4.7,
        'duracion_media': '00:23:10',
        'interaccion_media': '00:05:42',
        'tasa_registro': 16.6,
        'usuarios_con_intencion': 10000,
        'usuarios_registrados': 5000,
        'usuarios_totales': 15000,
        'usuarios_no_registrados': 5000,
    }
    
    # Mock: adjust based on number of selected countries
    if countries:
        all_countries = ["Argentina", "México", "España", "Colombia"]
        ratio = len(countries) / len(all_countries)
        kpis['sesiones_intencion'] = int(kpis['sesiones_intencion'] * ratio)
    
    # Format for display
    return {
        'Sesiones con Intención': f"{kpis['sesiones_intencion']:,}".replace(',', '.'),
        '% Rebote': f"{kpis['pct_rebote']:.1f}%".replace('.', ','),
        'Duración Media': kpis['duracion_media'],
        'Interacción Media': kpis['interaccion_media'],
        'Tasa de Registro': f"{kpis['tasa_registro']:.1f}%".replace('.', ','),
        'Usuarios con Intención': f"{kpis['usuarios_con_intencion']:,}".replace(',', '.'),
        'Usuarios Registrados': f"{kpis['usuarios_registrados']:,}".replace(',', '.'),
        'Usuarios Totales': f"{kpis['usuarios_totales']:,}".replace(',', '.'),
        'Usuarios No Registrados': f"{kpis['usuarios_no_registrados']:,}".replace(',', '.'),
    }
