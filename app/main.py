import streamlit as st
import pandas as pd
import os
from text_processor import TextPreprocessor
from model_trainer import ModelTrainer
from utils.visualization import create_confidence_gauge, create_key_features_chart

# Initialize processors
@st.cache_resource
def load_processors():
    text_processor = TextPreprocessor()
    model_trainer = ModelTrainer()
    
    # Load trained model if exists
    model_path = '../models/classifier.joblib'
    vectorizer_path = '../models/vectorizer.joblib'
    model_trainer.load_model(model_path, vectorizer_path)
    
    return text_processor, model_trainer

def main():
    st.set_page_config(page_title="Fake News Detector", layout="wide")
    
    st.title("Fake News Detector")
    
    # Load processors
    text_processor, model_trainer = load_processors()
    
    # Input methods
    input_method = st.radio("Choose input method:", ["Text Input", "File Upload"])
    
    if input_method == "Text Input":
        news_text = st.text_area("Enter news article text:", height=200)
        
        if st.button("Analyze") and news_text:
            with st.spinner("Analyzing..."):
                # Process text
                cleaned_text = text_processor.clean_text(news_text)
                
                # Get prediction
                prediction, confidence = model_trainer.predict(cleaned_text)
                
                # Display results in columns
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Classification Result")
                    result = "FAKE" if prediction == 1 else "REAL"
                    st.markdown(f"<h1 style='text-align: center; color: {'red' if prediction == 1 else 'green'};'>{result}</h1>", 
                              unsafe_allow_html=True)
                    
                    # Display confidence gauge
                    st.plotly_chart(create_confidence_gauge(confidence))
                
                with col2:
                    st.subheader("Key Features")
                    # Display key features chart
                    st.plotly_chart(create_key_features_chart(
                        cleaned_text, 
                        model_trainer.vectorizer
                    ))
    
    else:
        uploaded_file = st.file_uploader("Upload CSV file", type=['csv'])
        if uploaded_file and st.button("Analyze Batch"):
            df = pd.read_csv(uploaded_file)
            if 'text' in df.columns:
                with st.spinner("Analyzing batch..."):
                    # Process all texts
                    df = text_processor.process_data(df)
                    
                    # Get predictions
                    results = []
                    for text in df['cleaned_text']:
                        pred, conf = model_trainer.predict(text)
                        results.append({
                            'text': text[:100] + '...',
                            'prediction': 'FAKE' if pred == 1 else 'REAL',
                            'confidence': f"{conf*100:.2f}%"
                        })
                    
                    st.write("Batch Results:")
                    st.dataframe(pd.DataFrame(results))
            else:
                st.error("CSV must contain a 'text' column")

if __name__ == "__main__":
    main()