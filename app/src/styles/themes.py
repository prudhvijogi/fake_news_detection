def get_theme_variables():
    return """
        :root {
            --bg-primary: #ffffff;
            --bg-secondary: #f5f5f5;
            --text-primary: #1a1a1a;
            --text-secondary: #666666;
            --accent-color: #2196F3;
            --border-color: #e0e0e0;
        }
        
        [data-theme="dark"] {
            --bg-primary: #1a1a1a;
            --bg-secondary: #2d2d2d;
            --text-primary: #ffffff;
            --text-secondary: #b0b0b0;
            --accent-color: #64B5F6;
            --border-color: #404040;
        }
    """

def apply_theme_styles():
    return f"""
        <style>
        {get_theme_variables()}
        
        .stApp {{
            background-color: var(--bg-primary);
            color: var(--text-primary);
            transition: all 0.3s ease;
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Charts and visualizations */
        .js-plotly-plot {{
            background-color: var(--bg-secondary) !important;
        }}
        
        .js-plotly-plot .plotly .main-svg {{
            background-color: transparent !important;
        }}
        </style>
    """