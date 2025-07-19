from flask import Flask, render_template, request
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

app = Flask(__name__)
analyzer = SentimentIntensityAnalyzer()


@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    if request.method == 'POST':
        text = request.form['text']
        lang = request.form['lang']

        if not text.strip():
            result = {'error': 'No text was entered.'}
        else:
            if lang == 'en':
                score = analyzer.polarity_scores(text)['compound']
            elif lang == 'es':
                score = None  # No análisis en español con VADER

            words = [
                word.lower() for word in text.split()
                if word.isalpha() and len(word) > 3
            ]

            if not words:
                result = {'error': 'No keywords could be extracted.'}
            else:
                # Crear Word Cloud
                wc = WordCloud(width=800, height=400, background_color='white')
                wc.generate(' '.join(words))
                wc.to_file('static/wordcloud.png')

                result = {
                    'polarity': f"{score:.2f}" if score is not None else "N/A",
                    'keywords': list(set(words))
                }

    return render_template('index.html', result=result)
