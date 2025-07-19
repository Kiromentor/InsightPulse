from textblob import TextBlob

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # Usamos palabras filtradas como alternativa simple a noun_phrases
    keywords = list(set(
        word.lower() for word in blob.words if word.isalpha() and len(word) > 4
    ))[:10]  # Limitamos a 10 palabras

    return {
        "polarity": sentiment,
        "keywords": keywords
    }
