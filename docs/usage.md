# Usage Guide

## Single Article Analysis

1. **Access the Application**
   - Open web browser
   - Navigate to locally hosted application or deployed URL
   - Default local URL: http://localhost:8501

2. **Text Input Method**
   - Select "Text Input" option
   - Paste article text into text area
   - Click "Analyze" button
   - View results:
     * Classification (Fake/Real)
     * Confidence score
     * Key features visualization

3. **Batch Processing**
   - Select "File Upload" option
   - Prepare CSV file with 'text' column
   - Upload file through interface
   - Click "Analyze Batch"
   - View batch results table

## Interpreting Results

1. **Classification**
   - REAL: Article is likely legitimate
   - FAKE: Article shows characteristics of fake news

2. **Confidence Score**
   - 0-100% scale
   - Higher score indicates stronger confidence
   - Consider manual review for scores below 70%

3. **Key Features**
   - Bar chart shows important words/phrases
   - Length indicates feature importance
   - Use for understanding classification reasoning

## Best Practices

1. **Input Quality**
   - Provide complete article text
   - Ensure text is in English
   - Remove formatting when possible

2. **Batch Processing**
   - Limit batch size to 1000 articles
   - Ensure CSV format is correct
   - Wait for processing to complete

3. **Result Validation**
   - Cross-reference high-impact articles
   - Consider context and source
   - Use as tool, not sole determinant