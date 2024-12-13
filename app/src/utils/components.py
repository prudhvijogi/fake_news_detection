import streamlit as st
import plotly.graph_objects as go
from datetime import datetime

def create_theme_toggle(is_dark_mode):
    """Create theme toggle button"""
    icon = "🌙" if is_dark_mode else "☀️"
    text = "Light Mode" if is_dark_mode else "Dark Mode"
    return f"""
        <div class="theme-toggle" onclick="handleThemeToggle()">
            {icon} {text}
        </div>
        <script>
        function handleThemeToggle() {{
            const queryParams = new URLSearchParams(window.location.search);
            const currentTheme = queryParams.get('theme') || 'light';
            const newTheme = currentTheme === 'light' ? 'dark' : 'light';
            queryParams.set('theme', newTheme);
            window.location.search = queryParams.toString();
        }}
        </script>
    """

def create_header():
    """Create application header"""
    return """
        <div class="main-header">
            <h1 class="header-title">Fake News Detector</h1>
            <p class="header-subtitle">
                Analyze news articles using advanced machine learning algorithms
            </p>
        </div>
    """

def create_result_card(title, content, icon="📊"):
    """Create a styled result card"""
    return f"""
        <div class="result-card animate-fade-in">
            <div style="display: flex; align-items: center; gap: 1rem;">
                <div style="font-size: 1.5rem;">{icon}</div>
                <div>
                    <div style="font-weight: 600;">{title}</div>
                    <div>{content}</div>
                </div>
            </div>
        </div>
    """

def create_metric_card(label, value, delta=None, prefix="", suffix=""):
    """Create a metric card with optional delta"""
    delta_html = f"""
        <div style="color: {'#00C851' if delta > 0 else '#ff4444'}; font-size: 0.9rem;">
            {'+' if delta > 0 else ''}{delta}{suffix}
        </div>
    """ if delta is not None else ""
    
    return f"""
        <div class="metric-card animate-fade-in">
            <div class="metric-title">{label}</div>
            <div class="metric-value">{prefix}{value}{suffix}</div>
            {delta_html}
        </div>
    """

def create_progress_bar(progress, label=""):
    """Create a styled progress bar"""
    return f"""
        <div style="margin: 1rem 0;">
            <div style="margin-bottom: 0.5rem; font-size: 0.9rem;">{label}</div>
            <div class="progress-container">
                <div class="progress-bar" style="width: {progress}%;"></div>
            </div>
        </div>
    """

def create_confidence_gauge_v2(confidence_score):
    """Create an enhanced confidence gauge"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=confidence_score * 100,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#4CAF50"},
            'steps': [
                {'range': [0, 33], 'color': "#ffcdd2"},
                {'range': [33, 66], 'color': "#fff9c4"},
                {'range': [66, 100], 'color': "#c8e6c9"}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': 80
            }
        },
        title={'text': "Confidence Score"}
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)'
    )
    
    return fig

def store_analysis_history(text, result, confidence):
    """Store analysis history in session state"""
    if 'analysis_history' not in st.session_state:
        st.session_state.analysis_history = []
    
    st.session_state.analysis_history.append({
        'text': text[:100] + "..." if len(text) > 100 else text,
        'result': result,
        'confidence': confidence,
        'timestamp': datetime.now()
    })

def display_analysis_history():
    """Display analysis history"""
    if 'analysis_history' not in st.session_state or not st.session_state.analysis_history:
        st.info("No analysis history available")
        return
    
    for analysis in reversed(st.session_state.analysis_history[-5:]):
        st.markdown(create_result_card(
            title=f"Analysis from {analysis['timestamp'].strftime('%H:%M:%S')}",
            content=f"""
                Result: {analysis['result']} (Confidence: {analysis['confidence']:.1f}%)
                <br>Text: {analysis['text']}
            """,
            icon="📝"
        ), unsafe_allow_html=True)