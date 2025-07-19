# analysis/analyzer.py
from textblob import TextBlob
from textblob.exceptions import MissingCorpusError

def analyze_text(text, lang="en"):
    try:
        blob = TextBlob(text)

        if lang != "en":
            blob = blob.translate(to="en")

        sentiment = blob.sentiment.polarity

        keywords = [word.lower() for word in blob.words if word.isalpha() and len(word) > 4]

        return {
            "polarity": sentiment,
            "keywords": list(set(keywords))  # Elimina duplicados
        }
    except MissingCorpusError:
        return {
            "polarity": 0.0,
            "keywords": ["Missing required corpora. Run: python -m textblob.download_corpora"]
        }
    except Exception as e:
        return {
            "polarity": 0.0,
            "keywords": [f"Error: {str(e)}"]
        }
