from textblob import TextBlob

def analyze_text(text, lang="en"):
    blob = TextBlob(text)

    # Si el idioma es español, traducir al inglés
    if lang == "es":
        try:
            blob = blob.translate(to="en")
        except Exception as e:
            return {
                "error": f"Error al traducir el texto: {str(e)}",
                "polarity": None,
                "keywords": []
            }

    polarity = blob.sentiment.polarity
    keywords = [
        word.lower()
        for word in blob.words
        if word.isalpha() and len(word) > 4
    ]

    return {
        "polarity": polarity,
        "keywords": keywords
    }
