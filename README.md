# Fake News Detector

A machine learning-based system for detecting fake news articles using NLP techniques.

## Features
- Real-time text analysis
- Batch processing via CSV upload
- Interactive visualizations
- Confidence scoring
- Key feature identification

## Installation

1. Clone the repository:
```bash
git clone https://github.com/prudhvijogi/fake_news_detection
cd fake_news_detection
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
cd app
streamlit run main.py
```

## Usage

### Single Article Analysis
1. Choose "Text Input" option
2. Paste article text
3. Click "Analyze"

### Batch Processing
1. Choose "File Upload" option
2. Upload CSV file with 'text' column
3. Click "Analyze Batch"

## Project Structure
```
fake_news_detector/
├── app/                 # Application code
├── data/               # Data files
├── models/             # Trained models
├── notebooks/          # Jupyter notebooks
└── docs/              # Documentation
```

## Training New Model

To train a new model:
1. Place your dataset in `data/raw/`
2. Run the notebook in `notebooks/model_development.py`
3. Trained model will be saved in `models/`
