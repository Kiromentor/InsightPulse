from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import re

analyzer = SentimentIntensityAnalyzer()

def analyze_text(text):
    sentiment = analyzer.polarity_scores(text)["compound"]

    # Extrae palabras alfabéticas largas como keywords simples
    words = re.findall(r'\b[a-zA-Z]{5,}\b', text.lower())
    keywords = list(set(words))[:10]  # máximo 10 keywords únicas

    return {
        "polarity": sentiment,
        "keywords": keywords
    }
