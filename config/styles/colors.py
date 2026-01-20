"""
Global dashboard colors.
For use in pages that need colors without importing from a specific chart.
Each chart module has its own css.py with specific colors.
"""

# === GLOBAL COLORS ===
COLORS = {
    "primary": "#F28322",        # Primary orange
    "primary_dark": "#E65100",   # Dark orange
    "primary_light": "#F2C6A5",  # Light orange
    "secondary": "#2450A6",      # Primary blue
    "secondary_light": "#4E8ACF", # Light blue
    "background": "#ffffff",
    "grid": "#e0e0e0",
    "border": "#cccccc"
}

# === DEFAULT OPACITY ===
DEFAULT_OPACITY = 0.9


# === UTILITY FUNCTIONS ===
def hex_to_rgba(hex_color: str, opacity: float = DEFAULT_OPACITY) -> str:
    """
    Convert HEX color to RGBA with opacity.
    
    Args:
        hex_color: Color in HEX format (e.g., '#F28322' or 'F28322')
        opacity: Opacity value between 0 and 1 (default: 0.8)
        
    Returns:
        Color in RGBA format (e.g., 'rgba(242, 131, 34, 0.8)')
    """
    hex_color = hex_color.lstrip('#')
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    return f"rgba({r}, {g}, {b}, {opacity})"


def get_colors_with_opacity(opacity: float = DEFAULT_OPACITY) -> dict:
    """
    Get all global colors with opacity applied.
    
    Args:
        opacity: Opacity value between 0 and 1 (default: 0.8)
        
    Returns:
        Dict with all colors in RGBA format
    """
    return {
        key: hex_to_rgba(value, opacity) if value.startswith('#') else value
        for key, value in COLORS.items()
    }
