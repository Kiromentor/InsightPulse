import nltk
from textblob import download_corpora

# Descargar lo necesario para TextBlob
download_corpora.main()

# Si querés asegurarte de que esto no falle:
nltk.download("punkt")
nltk.download("brown")
nltk.download("wordnet")
