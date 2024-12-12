import nltk
from nltk.corpus import stopwords
import re
import pandas as pd

class TextPreprocessor:
    def __init__(self):
        # Download stopwords
        nltk.download('stopwords')
        self.stop_words = set(stopwords.words('english'))
    
    def clean_text(self, text):
        """Clean and preprocess the input text"""
        if not isinstance(text, str):
            return ""
            
        # Convert to lowercase
        text = text.lower()
        
        # Remove special characters and digits
        text = re.sub(r'[^a-zA-Z\s]', '', text)
        
        # Split into words (simple tokenization)
        tokens = text.split()
        
        # Remove stopwords
        tokens = [t for t in tokens if t not in self.stop_words]
        
        # Join tokens back into text
        return ' '.join(tokens)
    
    def process_data(self, df, text_column='text'):
        """Process all texts in a dataframe"""
        df['cleaned_text'] = df[text_column].apply(self.clean_text)
        return df