import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import numpy as np

class ModelTrainer:
    def __init__(self):
        self.device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
        self.model_name = "distilbert-base-uncased"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForSequenceClassification.from_pretrained(self.model_name, num_labels=2)
        self.model.to(self.device)
        self.model.eval()

    def predict(self, text):
        """Make prediction on processed text."""
        try:
            # Tokenize
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # Get prediction
            with torch.no_grad():
                outputs = self.model(**inputs)
                probabilities = torch.softmax(outputs.logits, dim=1)
                prediction = torch.argmax(probabilities, dim=1)
                confidence = torch.max(probabilities).item()

            return "FAKE" if prediction.item() == 1 else "REAL", confidence * 100

        except Exception as e:
            raise Exception(f"Prediction error: {str(e)}")

    def get_feature_importance(self, text):
        """Get feature importance scores."""
        try:
            # Tokenize
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            inputs = {k: v.to(self.device) for k, v in inputs.items()}

            # Get attention weights
            with torch.no_grad():
                outputs = self.model(**inputs, output_attentions=True)
                attention = outputs.attentions[-1].mean(dim=(0, 1)).cpu()

            # Get tokens
            tokens = self.tokenizer.convert_ids_to_tokens(inputs['input_ids'][0])

            # Get top features
            attention_scores = attention.numpy()
            top_indices = np.argsort(attention_scores)[-5:][::-1]
            
            return [(tokens[i], float(attention_scores[i])) for i in top_indices]

        except Exception as e:
            return None