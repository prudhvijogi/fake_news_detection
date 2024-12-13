import streamlit as st

def render_input_section():
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        text_input = st.text_area(
            "Input Article Text",
            height=200,
            placeholder="Enter article text here...",
            key="article_text"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="input-card">', unsafe_allow_html=True)
        file_upload = st.file_uploader(
            "Upload File",
            type=['txt', 'csv'],
            help="Drag and drop file here • TXT, CSV"
        )
        st.markdown('</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([0.4, 0.2, 0.4])
    with col2:
        analyze_button = st.button("Analyze", use_container_width=True)
    
    return text_input, file_upload, analyze_button