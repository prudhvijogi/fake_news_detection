import streamlit as st
import pandas as pd
import os
import io
from text_processor import TextPreprocessor
from model_trainer import ModelTrainer
from src.utils.visualization import create_confidence_gauge, create_key_features_chart

def apply_custom_style():
    st.markdown("""
        <style>
        /* Global styles */
        .stApp {
            background-color: #f5f5f5;
        }
        
        /* Header styling */
        .main-header {
            color: white;
            background-color: #1a1a1a;
            padding: 1rem;
            border-radius: 10px;
            margin-bottom: 2rem;
        }
        
        /* Input containers */
        .input-section {
            margin-bottom: 2rem;
        }
        
        .input-label {
            font-size: 1.2rem;
            color: #666;
            margin-bottom: 0.5rem;
        }
        
        /* Text area styling */
        .stTextArea textarea {
            background-color: #1f1f1f;
            color: white;
            border: none;
            border-radius: 10px;
            padding: 1rem;
            font-size: 1rem;
        }
        
        /* File uploader styling */
        .uploadfile {
            background-color: #1f1f1f;
            border: 2px dashed #666;
            border-radius: 10px;
            padding: 2rem;
            text-align: center;
            color: white;
        }
        
        .uploadfile:hover {
            border-color: #4CAF50;
        }
        
        /* Button styling */
        .stButton > button {
            background-color: #4CAF50 !important;
            color: white !important;
            padding: 0.75rem 2rem !important;
            border: none !important;
            border-radius: 5px !important;
            font-size: 1.1rem !important;
            width: 100% !important;
            margin-top: 1rem !important;
        }
        
        .stButton > button:hover {
            background-color: #45a049 !important;
        }
        
        /* Recent analysis section */
        .history-section {
            background-color: #1f1f1f;
            border-radius: 10px;
            padding: 1rem;
            margin-top: 2rem;
            color: white;
        }
        
        /* Results section */
        .results-container {
            background-color: #1f1f1f;
            border-radius: 10px;
            padding: 1.5rem;
            margin-top: 2rem;
            color: white;
        }
        
        /* Hide Streamlit branding */
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        
        /* File upload message */
        .upload-text {
            color: #666;
            font-size: 0.9rem;
            margin-top: 0.5rem;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    st.set_page_config(
        page_title="Fake News Detector",
        page_icon="🔍",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    apply_custom_style()
    
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