# Setup Instructions

## Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- Git

## Installation Steps

1. **Clone the Repository**
```bash
git clone https://github.com/prudhvijogi/fake_news_detection
cd fake—news–detection
```

2. **Create and Activate Virtual Environment**
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Download NLTK Data**
```python
python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords')"
```

5. **Prepare Data Directory**
```bash
mkdir -p data/raw data/processed models
```

6. **Train Model**
- Place your dataset in `data/raw/news_dataset.csv`
- Run the training notebook:
```bash
jupyter notebook notebooks/model_development.ipynb
```

7. **Run Application**
```bash
cd app
streamlit run main.py
```

## Troubleshooting

1. **Package Installation Issues**
   - Ensure you're using the correct Python version
   - Try upgrading pip: `pip install --upgrade pip`
   - Install packages individually if needed

2. **NLTK Data Issues**
   - Manually download NLTK data if automatic download fails
   - Check NLTK data directory permissions

3. **Model Loading Issues**
   - Ensure model files exist in models/ directory
   - Check file permissions