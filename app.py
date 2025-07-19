from flask import Flask, render_template, request
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import nltk

# Descarga automática de recursos necesarios (solo si faltan)
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

# Intenta descargar los datos de TextBlob
try:
    from textblob import download_corpora
    download_corpora.download_all()
except Exception as e:
    print("Warning: no se pudieron descargar los corpus de TextBlob:", e)

app = Flask(__name__)

# Ruta principal
@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    selected_lang = "en"

    if request.method == "POST":
        text = request.form["text"]
        selected_lang = request.form.get("language", "en")

        blob = TextBlob(text)

        try:
            if selected_lang == "es":
                blob = blob.translate(to="en")
        except Exception as e:
            print("No se pudo traducir:", e)

        polarity = blob.sentiment.polarity
        words = [word.lower() for word in blob.words if word.isalpha() and len(word) > 3]

        # Crear nube de palabras y guardarla
        wordcloud = WordCloud(width=800, height=400, background_color=None, mode="RGBA").generate(" ".join(words))
        wordcloud_path = os.path.join("static", "wordcloud.png")
        wordcloud.to_file(wordcloud_path)

        result = {
            "polarity": polarity,
            "keywords": list(set(words)),  # solo palabras únicas
            "image_path": wordcloud_path
        }

    return render_template("index.html", result=result, language=selected_lang)

if __name__ == "__main__":
    app.run(debug=True)
