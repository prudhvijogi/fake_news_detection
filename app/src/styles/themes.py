import streamlit as st

def apply_theme_styles():
    theme = st.session_state.get('theme', 'light')
    
    st.markdown(f"""
        <style>
        /* Theme variables */
        :root {{
            --bg-color: {('#f5f5f5' if theme == 'light' else '#1a1a1a')};
            --text-color: {('#333333' if theme == 'light' else '#ffffff')};
            --container-bg: {('#ffffff' if theme == 'light' else '#2d2d2d')};
            --border-color: {('#dddddd' if theme == 'light' else '#404040')};
            --input-text-color: {('#000000' if theme == 'light' else '#ffffff')};
            --heading-color: {('#000000' if theme == 'light' else '#ffffff')};
        }}
        
        /* Global styles */
        .stApp {{
            background-color: var(--bg-color);
            color: var(--text-color);
            transition: all 0.3s ease;
        }}
        
        /* Add more theme-specific styles here */
        </style>
    """, unsafe_allow_html=True)