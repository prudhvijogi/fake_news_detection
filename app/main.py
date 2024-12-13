import streamlit as st
import pandas as pd
import os
import io
from text_processor import TextPreprocessor
from model_trainer import ModelTrainer
from src.utils.visualization import create_confidence_gauge, create_key_features_chart

def initialize_theme():
    if 'theme' not in st.session_state:
        st.session_state.theme = 'light'

def apply_custom_style():
    st.markdown(f"""
        <style>
        /* Theme variables */
        :root {{
            --bg-color: {('#f5f5f5' if st.session_state.theme == 'light' else '#1a1a1a')};
            --text-color: {('#333333' if st.session_state.theme == 'light' else '#ffffff')};
            --container-bg: {('#ffffff' if st.session_state.theme == 'light' else '#2d2d2d')};
            --border-color: {('#dddddd' if st.session_state.theme == 'light' else '#404040')};
            --input-text-color: {('#000000' if st.session_state.theme == 'light' else '#ffffff')};
            --heading-color: {('#000000' if st.session_state.theme == 'light' else '#ffffff')};
        }}
        
        /* Global styles */
        .stApp {{
            background-color: var(--bg-color);
            transition: all 0.3s ease;
        }}
        
        /* Top-right controls container */
        .controls-container {{
            position: fixed;
            top: 1rem;
            right: 1rem;
            z-index: 1000;
            display: flex;
            gap: 1rem;
            align-items: center;
        }}
        
        /* GitHub link styling */
        .github-link {{
            color: var(--text-color);
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            width: 40px;
            height: 40px;
            background: var(--container-bg);
            border: 1px solid var(--border-color);
            border-radius: 50%;
            transition: all 0.3s ease;
        }}
        
        .github-link:hover {{
            transform: scale(1.1);
        }}
        
        /* GitHub icon color based on theme */
        .github-icon {{
            fill: var(--text-color);
        }}
        
        /* File uploader styling */
        .stFileUploader {{
            background-color: var(--container-bg) !important;
        }}
        
        /* Style the upload button specifically */
        .stFileUploader button {{
            background-color: var(--container-bg) !important;
            color: var(--text-color) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 5px !important;
        }}
        
        /* Style the upload text and drop target */
        .stFileUploader div[data-testid="stFileUploadDropzone"] {{
            background-color: var(--container-bg) !important;
            color: var(--text-color) !important;
            border: 2px dashed var(--border-color) !important;
            padding: 1rem !important;
        }}
        
        [data-testid="stFileUploadDropzone"] {{
            background-color: var(--container-bg) !important;
            color: var(--text-color) !important;
        }}
        
        /* Make the Streamlit button look like an icon */
        div[data-testid="stHorizontalBlock"] div[data-testid="column"] button {{
            background: var(--container-bg) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 50% !important;
            width: 40px !important;
            height: 40px !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
            cursor: pointer !important;
            font-size: 1.2rem !important;
            padding: 0 !important;
            transition: all 0.3s ease !important;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1) !important;
        }}
        
        div[data-testid="stHorizontalBlock"] div[data-testid="column"] button:hover {{
            transform: scale(1.1);
        }}
        
        /* Header styling */
        .main-header {{
            color: var(--heading-color);
            background-color: var(--container-bg);
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .main-header h1 {{
            color: var(--heading-color) !important;
            margin: 0;
        }}
        
        /* Input containers */
        .input-section {{
            margin-bottom: 2rem;
        }}
        
        .input-label {{
            font-size: 1.2rem;
            color: var(--text-color);
            margin-bottom: 0.5rem;
            font-weight: 500;
        }}
        
        /* Text area styling */
        .stTextArea textarea {{
            background-color: var(--container-bg) !important;
            color: var(--input-text-color) !important;
            border: 1px solid var(--border-color) !important;
            border-radius: 10px !important;
            padding: 1rem !important;
            font-size: 1rem !important;
        }}
        
        /* File uploader styling */
        .uploadfile {{
            background-color: var(--container-bg);
            border: 2px dashed var(--border-color);
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            color: var(--text-color);
        }}
        
        .uploadfile:hover {{
            border-color: #4CAF50;
        }}
        
        /* Button styling */
        .stButton > button {{
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 0.75rem 2rem !important;
            border: none !important;
            border-radius: 5px !important;
            font-size: 1.1rem !important;
            width: 100% !important;
            margin-top: 1rem !important;
        }}
        
        /* Analysis button specific styling */
        .analysis-button button {{
            width: 100% !important;
        }}
        
        .stButton > button:hover {{
            background-color: #45a049 !important;
        }}
        
        /* Recent analysis section */
        .history-section {{
            background-color: var(--container-bg);
            border-radius: 10px;
            padding: 1rem;
            margin-top: 2rem;
            color: var(--text-color);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        .history-section h3 {{
            color: var(--heading-color) !important;
            margin-bottom: 1rem;
        }}
        
        /* Results section */
        .results-container {{
            background-color: var(--container-bg);
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 2rem;
            color: var(--text-color);
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        /* Hide Streamlit branding */
        #MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        header {{visibility: hidden;}}
        
        /* File upload message */
        .upload-text {{
            color: var(--text-color);
            opacity: 0.7;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }}

        /* Warning message styling */
        .stAlert {{
            background-color: var(--container-bg) !important;
            color: var(--text-color) !important;
        }}
        </style>
    """, unsafe_allow_html=True)

def toggle_theme():
    st.session_state.theme = 'dark' if st.session_state.theme == 'light' else 'light'
    st.rerun()

def main():
    st.set_page_config(
        page_title="Fake News Detector",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    initialize_theme()
    apply_custom_style()
    
    # Container for the theme toggle and GitHub link
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 0.2, 0.2])
    with col5:
        theme_icon = "🌙" if st.session_state.theme == 'light' else "☀️"
        if st.button(theme_icon, key="theme_toggle"):
            toggle_theme()
    with col6:
        st.markdown(
            f'''
            <a href="https://github.com/prudhvijogi/fake_news_detection" target="_blank" class="github-link">
                <svg class="github-icon" height="24" width="24" viewBox="0 0 16 16">
                    <path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/>
                </svg>
            </a>
            ''',
            unsafe_allow_html=True
        )
    
    # Header
    st.markdown('<div class="main-header"><h1>Fake News Detector</h1></div>', unsafe_allow_html=True)
    
    # Main content
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="input-label">Input Article Text</div>', unsafe_allow_html=True)
        news_text = st.text_area(
            "",
            height=200,
            key="input_text",
            help="Enter article text here..."
        )
    
    with col2:
        st.markdown('<div class="input-label">Upload File</div>', unsafe_allow_html=True)
        uploaded_file = st.file_uploader(
            "",
            type=['txt', 'csv'],
            key="file_uploader",
            help="Drag and drop file here"
        )
        st.markdown(
            '<div class="upload-text">Limit 200MB per file • TXT, CSV</div>',
            unsafe_allow_html=True
        )
    
    # Analyze button
    if st.button("Analyze"):
        if news_text or uploaded_file:
            with st.spinner("Analyzing..."):
                # Your analysis code here
                st.markdown(
                    '<div class="results-container">Analysis results will appear here.</div>',
                    unsafe_allow_html=True
                )
        else:
            st.warning("Please enter text or upload a file to analyze")
    
    # Recent Analysis History
    st.markdown(
        '''
        <div class="history-section">
            <h3>Recent Article History</h3>
            <p>Previous analyses will appear here</p>
        </div>
        ''',
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()