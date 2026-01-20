BASIC_CARD_CSS = '''<div class="metric-card"><h3>{title}</h3><p>{value}</p></div>'''

CONTAINER_CSS = '''
    <style>
    .kpi-container {{
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 12px;
        margin-bottom: 16px;
        width: 100%;
    }}
    .metric-card {{
        background-color: #ffffff;
        border-radius: 8px;
        padding: 12px 20px;
        box-shadow: 0 4px 4px rgba(0,0,0,0.1);
        border-left: 4px solid #F28322;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        min-width: 150px;
        flex: 0 1 calc(20% - 12px); /* Máximo 5 cards por fila */
        max-width: calc(20% - 12px);
    }}
    .metric-card h3 {{
        color: #666666;
        font-size: 12px;
        font-weight: 500;
        margin: 0 0 6px 0;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        white-space: nowrap;
    }}
    .metric-card p {{
        color: #1a1a1a;
        font-size: 22px;
        font-weight: 700;
        margin: 0;
        line-height: 1;
        white-space: nowrap;
    }}
    </style>
    <div class="kpi-container">{cards_html}</div>
    '''