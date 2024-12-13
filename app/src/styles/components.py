import streamlit as st

def apply_component_styles():
    st.markdown("""
        <style>
        /* Component-specific styles */
        .main-header {
            padding: 2rem;
            text-align: center;
            margin-bottom: 2rem;
        }

        .prediction-box {
            padding: 1rem;
            border-radius: 10px;
            text-align: center;
            margin-bottom: 1rem;
        }

        .prediction-fake {
            background-color: rgba(255, 0, 0, 0.1);
            border: 2px solid #ff0000;
        }

        .prediction-real {
            background-color: rgba(0, 255, 0, 0.1);
            border: 2px solid #00ff00;
        }

        .confidence {
            font-size: 1.2rem;
            margin-top: 0.5rem;
        }

        /* Add more component styles here */
        </style>
    """, unsafe_allow_html=True)