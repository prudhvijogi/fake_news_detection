import streamlit as st

def render_results(analysis_results, visualizations):
    if not analysis_results:
        return

    st.markdown('<div class="results-section">', unsafe_allow_html=True)
    
    # Metrics row
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Classification</div>
                <div class="metric-value" style="color: {'red' if analysis_results['prediction'] == 'FAKE' else 'green'}">
                    {analysis_results['prediction']}
                </div>
            </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Confidence</div>
                <div class="metric-value">{analysis_results['confidence']*100:.1f}%</div>
            </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-title">Processing Time</div>
                <div class="metric-value">{analysis_results['processing_time']:.2f}s</div>
            </div>
        """, unsafe_allow_html=True)
    
    # Visualizations
    if visualizations:
        st.plotly_chart(visualizations['confidence_gauge'], use_container_width=True)
        st.plotly_chart(visualizations['key_features'], use_container_width=True)
    
    st.markdown('</div>', unsafe_allow_html=True)