import streamlit as st

def render_input_section():
    st.markdown('<div class="input-label">Input Article Text</div>', unsafe_allow_html=True)
    return st.text_area(
        "",
        height=200,
        key="input_text",
        help="Enter article text here..."
    )