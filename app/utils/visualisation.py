import plotly.express as px
import pandas as pd

def create_confidence_gauge(confidence_score):
    """Create a gauge chart for confidence score"""
    fig = px.pie(values=[confidence_score, 1-confidence_score], 
                 hole=0.7,
                 color_discrete_sequence=['#00CC96', '#EF553B'])
    fig.update_layout(
        showlegend=False,
        annotations=[dict(text=f"{confidence_score*100:.1f}%", 
                        x=0.5, y=0.5, 
                        font_size=20, 
                        showarrow=False)])
    return fig

def create_key_features_chart(text, vectorizer, top_n=5):
    """Create bar chart of key features"""
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
    fig = px.bar(features_df, 
                 x='weight', 
                 y='feature',
                 orientation='h')
    
    return fig