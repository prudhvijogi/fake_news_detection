def get_theme_styles(is_dark_mode):
    """Get theme-specific styles"""
    if is_dark_mode:
        return {
            'bg_color': '#1a1a1a',
            'text_color': '#ffffff',
            'secondary_bg': '#2d2d2d',
            'accent_color': '#4CAF50',
            'accent_hover': '#45a049',
            'border_color': '#404040',
            'input_bg': '#333333',
            'error_color': '#ff4444',
            'success_color': '#00C851',
            'warning_color': '#ffbb33',
            'info_color': '#33b5e5'
        }
    else:
        return {
            'bg_color': '#ffffff',
            'text_color': '#333333',
            'secondary_bg': '#f5f5f5',
            'accent_color': '#2e7d32',
            'accent_hover': '#1b5e20',
            'border_color': '#e0e0e0',
            'input_bg': '#ffffff',
            'error_color': '#f44336',
            'success_color': '#4CAF50',
            'warning_color': '#ff9800',
            'info_color': '#2196f3'
        }

def get_css(theme):
    """Generate CSS based on theme"""
    return f"""
        <style>
        /* Global styles */
        .stApp {{
            background-color: {theme['bg_color']};
            color: {theme['text_color']};
        }}
        
        /* Theme toggle button */
        .theme-toggle {{
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 1000;
            background-color: {theme['secondary_bg']};
            border: 1px solid {theme['border_color']};
            border-radius: 20px;
            padding: 0.5rem 1rem;
            cursor: pointer;
            transition: all 0.3s ease;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .theme-toggle:hover {{
            background-color: {theme['accent_color']};
            color: white;
        }}
        
        /* Header styling */
        .main-header {{
            background-color: {theme['secondary_bg']};
            padding: 2rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .header-title {{
            color: {theme['text_color']};
            font-size: 2.5rem;
            font-weight: 700;
            margin: 0;
        }}
        
        .header-subtitle {{
            color: {theme['text_color']}aa;
            font-size: 1.1rem;
            margin-top: 0.5rem;
        }}
        
        /* Input containers */
        .input-container {{
            background-color: {theme['secondary_bg']};
            padding: 1.5rem;
            border-radius: 10px;
            margin-bottom: 1rem;
        }}
        
        .input-label {{
            color: {theme['text_color']};
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }}
        
        /* Text area styling */
        .stTextArea textarea {{
            background-color: {theme['input_bg']} !important;
            color: {theme['text_color']} !important;
            border: 1px solid {theme['border_color']} !important;
            border-radius: 8px !important;
            padding: 1rem !important;
            font-size: 1rem !important;
            transition: all 0.3s ease !important;
        }}
        
        .stTextArea textarea:focus {{
            border-color: {theme['accent_color']} !important;
            box-shadow: 0 0 0 2px {theme['accent_color']}33 !important;
        }}
        
        /* File uploader styling */
        .uploadfile {{
            background-color: {theme['input_bg']};
            border: 2px dashed {theme['border_color']};
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            transition: all 0.3s ease;
        }}
        
        .uploadfile:hover {{
            border-color: {theme['accent_color']};
        }}
        
        /* Button styling */
        .stButton > button {{
            background-color: {theme['accent_color']} !important;
            color: white !important;
            padding: 0.75rem 2rem !important;
            border: none !important;
            border-radius: 8px !important;
            font-size: 1.1rem !important;
            font-weight: 600 !important;
            width: 100% !important;
            transition: all 0.3s ease !important;
        }}
        
        .stButton > button:hover {{
            background-color: {theme['accent_hover']} !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 12px {theme['accent_color']}66;
        }}
        
        /* Results section */
        .results-container {{
            background-color: {theme['secondary_bg']};
            border-radius: 10px;
            padding: 2rem;
            margin-top: 2rem;
        }}
        
        .result-card {{
            background-color: {theme['input_bg']};
            border-radius: 8px;
            padding: 1.5rem;
            margin-bottom: 1rem;
            border: 1px solid {theme['border_color']};
            transition: all 0.3s ease;
        }}
        
        .result-card:hover {{
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }}
        
        /* Metrics styling */
        .metric-container {{
            display: flex;
            gap: 1rem;
            flex-wrap: wrap;
        }}
        
        .metric-card {{
            background-color: {theme['input_bg']};
            border-radius: 8px;
            padding: 1rem;
            flex: 1;
            min-width: 200px;
            border: 1px solid {theme['border_color']};
        }}
        
        .metric-title {{
            font-size: 0.9rem;
            color: {theme['text_color']}aa;
            margin-bottom: 0.5rem;
        }}
        
        .metric-value {{
            font-size: 1.5rem;
            font-weight: 600;
            color: {theme['text_color']};
        }}
        
        /* Progress bar */
        .progress-container {{
            width: 100%;
            height: 4px;
            background-color: {theme['border_color']};
            border-radius: 2px;
            overflow: hidden;
        }}
        
        .progress-bar {{
            height: 100%;
            background-color: {theme['accent_color']};
            transition: width 0.3s ease;
        }}
        
        /* Hide Streamlit elements */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* Animations */
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(10px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
        
        .animate-fade-in {{
            animation: fadeIn 0.5s ease forwards;
        }}
        </style>
    """