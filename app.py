from flask import Flask, render_template, request
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

app = Flask(__name__)

def generate_wordcloud(keywords):
    # Convierte la lista en un string separado por espacios
    text = " ".join(keywords)

    # Ruta a la imagen del mapa
    mask_path = os.path.join("static", "img", "world_map.png")
    mask = np.array(Image.open(mask_path))

    # Crea la nube de palabras con la máscara del mapa
    wordcloud = WordCloud(
        background_color="white",
        mask=mask,
        contour_width=1,
        contour_color="black",
        colormap="cool",
        width=mask.shape[1],
        height=mask.shape[0]
    ).generate(text)

    # Guarda la imagen resultante
    output_path = os.path.join("static", "wordcloud.png")
    wordcloud.to_file(output_path)
    return output_path

def analyze_text(text, lang):
    if lang == "en":
        # Análisis con VADER para inglés
        analyzer = SentimentIntensityAnalyzer()
        scores = analyzer.polarity_scores(text)
        polarity = scores["compound"]
        blob = TextBlob(text)
        keywords = [word.lower() for word in blob.words if word.isalpha() and len(word) > 4]
    elif lang == "es":
        # Solo keywords y polaridad simple (no VADER)
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        keywords = [word.lower() for word in blob.words if word.isalpha() and len(word) > 4]
    else:
        polarity = 0.0
        keywords = []

    wordcloud_path = generate_wordcloud(keywords)

    return {
        "polarity": polarity,
        "keywords": keywords,
        "wordcloud_path": wordcloud_path
    }

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    selected_lang = "en"
    if request.method == "POST":
        text = request.form["text"]
        selected_lang = request.form["language"]
        result = analyze_text(text, selected_lang)

    return render_template("index.html", result=result, selected_lang=selected_lang)

