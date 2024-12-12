# API Documentation

## Core Classes

### TextPreprocessor

```python
class TextPreprocessor:
    def __init__(self):
        """Initialize preprocessor with NLTK components"""
    
    def clean_text(self, text: str) -> str:
        """Clean and preprocess single text"""
        
    def process_data(self, df: pd.DataFrame, text_column: str = 'text') -> pd.DataFrame:
        """Process all texts in dataframe"""
```

### ModelTrainer

```python
class ModelTrainer:
    def __init__(self):
        """Initialize with TF-IDF vectorizer and classifier"""
    
    def train(self, df: pd.DataFrame, text_column: str = 'cleaned_text',
              label_column: str = 'label') -> None:
        """Train model with provided data"""
    
    def predict(self, text: str) -> Tuple[int, float]:
        """Predict class and confidence for text"""
```

### Visualization Functions

```python
def create_confidence_gauge(confidence_score: float) -> Figure:
    """Create confidence score visualization"""

def create_key_features_chart(text: str, vectorizer: TfidfVectorizer,
                            top_n: int = 5) -> Figure:
    """Create key features visualization"""
```

## Usage Examples

```python
# Initialize components
preprocessor = TextPreprocessor()
trainer = ModelTrainer()

# Process single text
cleaned_text = preprocessor.clean_text("Article text here...")

# Make prediction
prediction, confidence = trainer.predict(cleaned_text)
```

## Data Formats

1. **Input Text**
   - String format
   - English language
   - Raw article text

2. **CSV Format**
   - Required columns:
     * text: Article content
     * label: 0 (real) or 1 (fake)

3. **Model Output**
   - Prediction: 0 or 1
   - Confidence: Float 0-1

## Error Handling

The API includes error handling for:
- Invalid input formats
- Missing data
- Model loading issues
- Processing errors