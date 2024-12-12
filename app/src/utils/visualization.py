import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def create_confidence_gauge(confidence_score):
    """
    Create a gauge chart for confidence score visualization
    
    Args:
        confidence_score (float): Prediction confidence between 0 and 1
        
    Returns:
        plotly.graph_objects.Figure: Gauge chart figure
    """
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = confidence_score * 100,
        domain = {'x': [0, 1], 'y': [0, 1]},
        gauge = {
            'axis': {'range': [0, 100]},
            'bar': {'color': "#1f77b4"},
            'steps': [
                {'range': [0, 33], 'color': "#ff7f0e"},
                {'range': [33, 66], 'color': "#ffbb78"},
                {'range': [66, 100], 'color': "#2ca02c"}
            ]
        }
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10),
        title={
            'text': "Confidence Score",
            'y':0.9,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'
        }
    )
    
    return fig

def create_key_features_chart(text, vectorizer, top_n=5):
    """
    Create bar chart of key features from the text
    
    Args:
        text (str): Input text
        vectorizer: TF-IDF vectorizer
        top_n (int): Number of top features to display
        
    Returns:
        plotly.graph_objects.Figure: Bar chart figure
    """
    # Get feature names and their weights
    feature_names = vectorizer.get_feature_names_out()
    feature_weights = vectorizer.transform([text]).toarray()[0]
    
    # Create dataframe of features and weights
    features_df = pd.DataFrame({
        'feature': feature_names,
        'weight': feature_weights
    })
    
    # Sort and get top features
    features_df = features_df.nlargest(top_n, 'weight')
    
    # Create bar chart
    fig = px.bar(
        features_df,
        x='weight',
        y='feature',
        orientation='h',
        title='Key Features Analysis'
    )
    
    fig.update_layout(
        height=300,
        margin=dict(l=10, r=10, t=40, b=10),
        yaxis_title="",
        xaxis_title="Feature Importance",
        showlegend=False
    )
    
    return fig

def create_reliability_metrics(prediction_proba):
    """
    Create reliability metrics visualization
    
    Args:
        prediction_proba (float): Prediction probability
        
    Returns:
        plotly.graph_objects.Figure: Metrics visualization
    """
    reliability_score = prediction_proba * 100
    
    fig = go.Figure()
    
    # Add reliability score
    fig.add_trace(go.Indicator(
        mode="number+gauge",
        value=reliability_score,
        domain={'x': [0, 1], 'y': [0, 0.5]},
        title={'text': "Reliability Score"},
        gauge={
            'shape': "bullet",
            'axis': {'range': [None, 100]},
            'threshold': {
                'line': {'color': "red", 'width': 2},
                'thickness': 0.75,
                'value': 80
            },
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 80], 'color': "gray"}
            ],
            'bar': {'color': "black"}
        }
    ))
    
    fig.update_layout(
        height=250,
        margin=dict(l=10, r=10, t=40, b=10)
    )
    
    return fig