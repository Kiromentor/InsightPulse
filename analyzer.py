# analysis/analyzer.py
from textblob import TextBlob
import nltk nltk.download('punkt')  # Solo si hace falta (Render puede fallar sin esto)


def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    return {
        "polarity": sentiment,
        "keywords": [word.lower() for word in blob.noun_phrases]
    }
