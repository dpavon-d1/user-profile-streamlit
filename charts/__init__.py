"""
Dashboard charts module.
Contains functions that return Plotly figures.
"""

from .funnel import create_funnel_chart
from .maps import create_map, get_map_config
from .bar_charts import create_bar_chart, create_stacked_bar_chart
from .line_charts import create_line_chart
from .heatmaps import create_heatmap_table, style_dataframe_heatmap
from .kpi_cards import render_kpi_row

