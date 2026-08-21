import pickle
import re
from pathlib import Path
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


BASE_DIR = Path(__file__).resolve().parent

MODEL_PATH = BASE_DIR / "lstm_sentiment_model.keras"
TOKENIZER_PATH = BASE_DIR / "tokenizer.pkl"


with open(TOKENIZER_PATH, "rb") as f:
    tokenizer = pickle.load(f)


model = load_model(MODEL_PATH)


# Creating stopwords
nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Preprocessing Function
def preprocess(text):
    # Changing all the review message to lower case
    text = text.lower()
    # Removing punctuations from the review message
    text = re.sub(r"[^\w\s]", "", text)
    # replace digits with no space
    text = re.sub(r"\d", "", text)

    # Tokenization
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]

    # joining back the tokens for token indexing and sequencing
    text = " ".join(tokens)

    # Tokenize using our downloaded Tokenizer
    X = tokenizer.texts_to_sequences(text)

    # Padding
    padded_text = pad_sequences(X, maxlen = 310,  padding = 'post', truncating = 'post')


    return padded_text


# Prediction Function
def predict_sentiment(processed_text):
    prediction = model.predict(processed_text)
    sentiment = int(prediction[0][0] >= 0.5)

    if sentiment == 1:
        sentiment = "Positive"
    else:
        sentiment = "Negative"

    return sentiment
