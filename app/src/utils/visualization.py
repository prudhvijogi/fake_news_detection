import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st

def create_confidence_gauge(confidence_score):
    """Create a gauge chart for confidence score."""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=confidence_score,
        domain={'x': [0, 1], 'y': [0, 1]},
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1f77b4"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [0, 30], 'color': '#ffcccb'},
                {'range': [30, 70], 'color': '#ffffcc'},
                {'range': [70, 100], 'color': '#90EE90'}
            ],
        },
        title={'text': "Confidence Score"}
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        font={'color': '#808495'}
    )
    
    st.plotly_chart(fig, use_container_width=True)

def create_key_features_chart(features):
    """Create a horizontal bar chart for feature importance."""
    if not features:
        return
    
    # Create DataFrame from features
    df = pd.DataFrame(features, columns=['Feature', 'Importance'])
    
    # Create horizontal bar chart
    fig = px.bar(
        df,
        x='Importance',
        y='Feature',
        orientation='h',
        title='Feature Importance'
    )
    
    # Update layout
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#808495'},
        showlegend=False
    )
    
    # Update axes
    fig.update_xaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='rgba(128,128,128,0.2)',
        zeroline=False
    )
    fig.update_yaxes(
        showgrid=False,
        zeroline=False
    )
    
    st.plotly_chart(fig, use_container_width=True)

def plot_analysis_history(history_data):
    """Create a line chart for analysis history."""
    if not history_data:
        return
    
    df = pd.DataFrame(history_data)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    fig = px.line(
        df,
        x='timestamp',
        y='confidence',
        color='prediction',
        title='Analysis History'
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=50, b=10),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font={'color': '#808495'}
    )
    
    st.plotly_chart(fig, use_container_width=True)