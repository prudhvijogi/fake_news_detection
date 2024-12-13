import streamlit as st

def render_header():
    st.markdown(
        '''
        <div class="main-header">
            <h1>Fake News Detector</h1>
            <p>Detect fake news using advanced machine learning</p>
        </div>
        ''',
        unsafe_allow_html=True
    )