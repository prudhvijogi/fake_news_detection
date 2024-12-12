from setuptools import setup, find_packages

setup(
    name="fake_news_detector",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        'streamlit>=1.15.0',
        'pandas>=1.5.0',
        'numpy>=1.23.0',
        'scikit-learn>=1.0.2',
        'nltk>=3.7',
        'joblib>=1.2.0',
        'plotly>=5.11.0',
        'python-dotenv>=0.21.0'
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A machine learning system for detecting fake news",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/fake-news-detector",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)