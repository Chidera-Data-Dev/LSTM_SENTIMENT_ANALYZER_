# LSTM Sentiment Analysis

## Overview

A Natural Language Processing project that uses an LSTM neural network to classify text sentiment as **Positive** or **Negative**.

The project covers text preprocessing, tokenization, sequence padding, LSTM model training, evaluation, and deployment.

## Model Performance

The LSTM model achieved **77.45% test accuracy** on unseen data.

## Deployment

The trained model is exposed through a **FastAPI REST API** and connected to a **Streamlit frontend** for real-time sentiment prediction.

### Flow

User Input → Streamlit → FastAPI → LSTM Model → Sentiment Prediction

## Recommendations & Future Improvements

The current model provides a solid baseline for sentiment classification. Future improvements could include:

- Experimenting with pretrained word embeddings.
- Testing more advanced NLP architectures.
- Improving text preprocessing.
- Training with a larger and more diverse dataset.
- Monitoring real-world predictions to identify areas for improvement.

## Technologies

- Python
- TensorFlow / Keras
- NLTK
- NumPy
- FastAPI
- Streamlit
- Uvicorn

DATASET LINK: https://www.kaggle.com/datasets/mwallerphunware/imbd-movie-reviews-for-binary-sentiment-analysis
