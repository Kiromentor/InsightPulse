# analysis/analyzer.py
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

def analyze_text(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    # keywords básicas
    keywords = [word.lower() for word in blob.words if word.isalpha() and len(word) > 4]

    # generar nube de palabras
    wordcloud = WordCloud(width=800, height=400, background_color="white").generate(" ".join(keywords))
    image_path = os.path.join("static", "wordcloud.png")
    wordcloud.to_file(image_path)

    return {
        "polarity": sentiment,
        "keywords": keywords,
        "wordcloud_image": image_path
    }
