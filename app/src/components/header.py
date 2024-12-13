import streamlit as st

def render_header(theme):
    st.markdown(f"""
        <div class="header">
            <h1 class="header-title">Fake News Detector</h1>
        </div>
    """, unsafe_allow_html=True)