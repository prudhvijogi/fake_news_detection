# Save this as fake_news_detection/notebooks/model_development.py

import sys
import os
# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
import joblib

# Download required NLTK data
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')

# Import local modules
from app.text_processor import TextPreprocessor
from app.model_trainer import ModelTrainer

def create_directories():
    """Create necessary directories if they don't exist"""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    directories = [
        os.path.join(base_dir, 'data/processed'),
        os.path.join(base_dir, 'models')
    ]
    for directory in directories:
        if not os.path.exists(directory):
            os.makedirs(directory)

def load_data(filepath):
    """Load and prepare the dataset"""
    try:
        # Try different encodings
        try:
            df = pd.read_csv(filepath, encoding='utf-8')
        except UnicodeDecodeError:
            try:
                df = pd.read_csv(filepath, encoding='latin-1')
            except UnicodeDecodeError:
                df = pd.read_csv(filepath, encoding='cp1252')
        
        # Convert Label to binary (TRUE -> 1, FALSE -> 0)
        df['Label'] = (df['Label'] == 'TRUE').astype(int)
        
        print("\nDataset Information:")
        print(f"Shape: {df.shape}")
        print("\nLabel Distribution:")
        print(df['Label'].value_counts())
        
        return df
    
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def preprocess_data(df):
    """Preprocess the text data"""
    try:
        preprocessor = TextPreprocessor()
        df = preprocessor.process_data(df, text_column='Statement')
        print("\nPreprocessing completed successfully")
        return df
    except Exception as e:
        print(f"Error in preprocessing: {str(e)}")
        return None

def train_and_evaluate_model(df):
    """Train the model and evaluate its performance"""
    try:
        # Initialize trainer
        trainer = ModelTrainer()
        
        # Split data
        X = df['cleaned_text']
        y = df['Label']
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )
        
        # Train model
        print("\nTraining model...")
        trainer.train(pd.DataFrame({'cleaned_text': X_train, 'label': y_train}))
        
        # Make predictions
        print("\nEvaluating model...")
        y_pred = [trainer.predict(text)[0] for text in X_test]
        
        # Print classification report
        print("\nClassification Report:")
        print(classification_report(y_test, y_pred))
        
        # Plot confusion matrix
        plt.figure(figsize=(8, 6))
        cm = confusion_matrix(y_test, y_pred)
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
        plt.title('Confusion Matrix')
        plt.ylabel('True Label')
        plt.xlabel('Predicted Label')
        
        # Save confusion matrix
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        plt.savefig(os.path.join(base_dir, 'docs/confusion_matrix.png'))
        plt.close()
        
        # Save model
        print("\nSaving model...")
        model_path = os.path.join(base_dir, 'models/classifier.joblib')
        vectorizer_path = os.path.join(base_dir, 'models/vectorizer.joblib')
        trainer.save_model(model_path, vectorizer_path)
        
        # Example predictions
        print("\nExample Predictions:")
        for i in range(5):
            text = X_test.iloc[i]
            true_label = y_test.iloc[i]
            pred_label, conf = trainer.predict(text)
            print(f"\nText: {text[:100]}...")
            print(f"True Label: {'REAL' if true_label == 1 else 'FAKE'}")
            print(f"Predicted: {'REAL' if pred_label == 1 else 'FAKE'} (Confidence: {conf:.2f})")
        
        return trainer
        
    except Exception as e:
        print(f"Error in model training/evaluation: {str(e)}")
        return None

def main():
    """Main execution function"""
    print("Starting model development process...")
    
    # Create necessary directories
    create_directories()
    
    # Get base directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    # Load data
    data_path = os.path.join(base_dir, 'data/raw/news_dataset.csv')
    df = load_data(data_path)
    if df is None:
        return
    
    # Preprocess data
    df = preprocess_data(df)
    if df is None:
        return
    
    # Save processed data
    processed_data_path = os.path.join(base_dir, 'data/processed/cleaned_data.csv')
    df.to_csv(processed_data_path, index=False)
    
    # Train and evaluate model
    trainer = train_and_evaluate_model(df)
    if trainer is None:
        return
    
    print("\nModel development completed successfully!")

if __name__ == "__main__":
    main()