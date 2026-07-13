import streamlit as st

def inject_custom_css():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* Hide Streamlit default components and menus */
        #MainMenu {visibility: hidden !important;}
        footer {visibility: hidden !important;}
        header {visibility: hidden !important;}
        div[data-testid="stHeader"] {display: none !important;}
        div[data-testid="stAppDeployButton"] {display: none !important;}
        button[title="View source code"] {display: none !important;}
        
        /* Layout overrides */
        html, body, [class*="css"] {
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
            background-color: #F8F6F2 !important;
            color: #2C2C2C !important;
        }
        .stApp {
            background-color: #F8F6F2 !important;
        }
        
        /* Page container padding adjustments */
        div.block-container {
            padding-top: 1.5rem !important;
            padding-bottom: 1.5rem !important;
            max-width: 92% !important;
        }
        
        /* Sidebar styling overrides */
        section[data-testid="stSidebar"] {
            background-color: #F2EEE8 !important;
            border-right: 1px solid #E6DED3 !important;
        }
        section[data-testid="stSidebar"] [class*="css"] {
            color: #2C2C2C !important;
        }
        
        /* Card components styling (white cards on warm neutral backgrounds) */
        .analytics-card {
            background-color: #FFFFFF;
            border: 1px solid #E6DED3;
            border-radius: 4px;
            padding: 16px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.02);
            margin-bottom: 12px;
            min-height: 95px;
        }
        .analytics-card-title {
            font-size: 11px;
            font-weight: 500;
            color: #777777;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            margin-bottom: 6px;
        }
        .analytics-card-value {
            font-size: 24px;
            font-weight: 700;
            color: #2C2C2C;
            line-height: 1.2;
        }
        .analytics-card-sub {
            font-size: 11px;
            color: #777777;
            margin-top: 6px;
        }
        
        .trend-positive {
            color: #5D7357;
            font-weight: 600;
        }
        .trend-negative {
            color: #A65A52;
            font-weight: 600;
        }
        .trend-warning {
            color: #B78C4C;
            font-weight: 600;
        }
        
        /* Section headers */
        .section-header {
            font-size: 13px;
            font-weight: 600;
            color: #2C2C2C;
            border-bottom: 1px solid #E6DED3;
            padding-bottom: 4px;
            margin-top: 22px;
            margin-bottom: 14px;
            text-transform: uppercase;
            letter-spacing: 0.8px;
        }
        
        /* Custom Business Insights Box */
        .insight-box {
            background-color: #FFFFFF;
            border: 1px solid #E6DED3;
            border-radius: 4px;
            padding: 18px;
            min-height: 350px;
            height: 100%;
        }
        .insight-title {
            font-size: 12px;
            font-weight: 600;
            color: #2C2C2C;
            margin-bottom: 14px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }
        .insight-item {
            font-size: 12px;
            line-height: 1.6;
            color: #2C2C2C;
            margin-bottom: 12px;
            border-left: 2px solid #E6DED3;
            padding-left: 10px;
        }
        .insight-item:last-child {
            margin-bottom: 0;
        }
        
        /* Zebra-striped clean table styling */
        .table-container {
            border: 1px solid #E6DED3;
            border-radius: 4px;
            background-color: #FFFFFF;
            overflow: hidden;
            margin-bottom: 16px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            font-size: 12px;
            color: #2C2C2C;
        }
        th {
            background-color: #F2EEE8 !important;
            color: #2C2C2C !important;
            font-weight: 600 !important;
            border-bottom: 1px solid #E6DED3 !important;
            padding: 10px 12px !important;
            text-align: left !important;
        }
        td {
            padding: 10px 12px !important;
            border-bottom: 1px solid #E6DED3 !important;
            background-color: #FFFFFF !important;
        }
        tr:last-child td {
            border-bottom: none !important;
        }
        tr:nth-child(even) td {
            background-color: #F8F6F2 !important;
        }
    </style>
    """, unsafe_allow_html=True)

def inject_nav_css(active_page_index):
    st.markdown(f"""
    <style>
        /* Style navigation buttons default state */
        div[data-testid="stHorizontalBlock"]:first-of-type button {{
            background-color: #FFFFFF !important;
            border: 1px solid #E6DED3 !important;
            border-bottom: 2px solid #E6DED3 !important;
            color: #777777 !important;
            font-weight: 500 !important;
            border-radius: 4px !important;
            height: 38px !important;
            transition: all 0.2s ease !important;
        }}
        div[data-testid="stHorizontalBlock"]:first-of-type button:hover {{
            border-color: #5D7357 !important;
            color: #5D7357 !important;
        }}
        /* Style active navigation button */
        div[data-testid="stHorizontalBlock"]:first-of-type div[data-testid="column"]:nth-child({active_page_index}) button {{
            border-color: #5D7357 !important;
            border-bottom: 2px solid #5D7357 !important;
            color: #2C2C2C !important;
            font-weight: 600 !important;
            background-color: #F2EEE8 !important;
        }}
    </style>
    """, unsafe_allow_html=True)

def render_kpi_card(title, value, subtitle, trend_type=None, trend_val=None):
    trend_html = ""
    if trend_type == "pos":
        trend_html = f"<span class='trend-positive'>↑ {trend_val}</span>"
    elif trend_type == "neg":
        trend_html = f"<span class='trend-negative'>↓ {trend_val}</span>"
    elif trend_type == "warn":
        trend_html = f"<span class='trend-warning'>{trend_val}</span>"
        
    sub_text = f"{trend_html} {subtitle}" if trend_html else subtitle
    
    card_content = f"""
    <div class="analytics-card">
        <div class="analytics-card-title">{title}</div>
        <div class="analytics-card-value">{value}</div>
        <div class="analytics-card-sub">{sub_text}</div>
    </div>
    """
    st.markdown(card_content, unsafe_allow_html=True)
