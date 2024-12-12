from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib
import os
import pandas as pd

class ModelTrainer:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=5000)
        self.model = LogisticRegression(random_state=42)
        
    def train(self, df, text_column='cleaned_text', label_column='label'):
        """Train the model with provided data"""
        # Create feature vectors
        X = self.vectorizer.fit_transform(df[text_column])
        y = df[label_column]
        
        # Train model
        self.model.fit(X, y)
        
    def save_model(self, model_path, vectorizer_path):
        """Save the trained model and vectorizer"""
        joblib.dump(self.model, model_path)
        joblib.dump(self.vectorizer, vectorizer_path)
        
    def load_model(self, model_path, vectorizer_path):
        """Load trained model and vectorizer"""
        if os.path.exists(model_path) and os.path.exists(vectorizer_path):
            self.model = joblib.load(model_path)
            self.vectorizer = joblib.load(vectorizer_path)
            return True
        return False
    
    def predict(self, text):
        """Make prediction on text"""
        # Transform text to vector
        vector = self.vectorizer.transform([text])
        # Get prediction and probability
        prediction = self.model.predict(vector)
        probability = self.model.predict_proba(vector)
        return prediction[0], max(probability[0])