# analysis/analyzer.py
from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    return {
        "polarity": sentiment,
        "keywords": [word.lower() for word in blob.noun_phrases]
    }
