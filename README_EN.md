
# InsightPulse 🧠✨

Sentiment Analysis and Keyword Extraction using Flask + TextBlob + NLTK

---

## 📌 What is InsightPulse?

**InsightPulse** is a simple yet powerful web application that allows users to analyze input text to:

* Detect **sentiment** (polarity: positive, negative, or neutral)
* Extract significant **keywords** (nouns or key phrases)

It is built with Python, Flask, and uses natural language processing (NLP) libraries like **TextBlob** and **NLTK**.

---

## 🚀 What is it for?

This project is perfect for:

* Practicing text processing in Python
* Understanding basic NLP concepts
* Creating a real-time text analysis web app
* Showcasing as a practical example in your portfolio

---

## 🧰 Technologies Used

* Python 3.13+
* Flask
* TextBlob
* NLTK
* HTML + TailwindCSS (CDN)
* Render (for free deployment)

---

## 📷 Screenshot

*Add a screenshot or GIF of the project running here*

---

## ⚙️ How to Run the Project

### 1. Clone the repository

```bash
git clone https://github.com/Kiromentor/InsightPulse
cd insightpulse
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Download NLTK and TextBlob corpora

```python
# In Python interactive mode
import nltk
nltk.download('punkt')
nltk.download('brown')

# Or use:
python -m textblob.download_corpora
```

### 4. Run the app

```bash
flask run
```

---

## 🌐 Deploy on Render

Render requires:

* `requirements.txt`
* `app.py`
* a `render.yaml` file (optional)
* use of `gunicorn` as the start command (`gunicorn app:app`)

---

## 🤝 Contributions

Contributions are welcome! If you want to improve the UI, add new analyses, or integrate external APIs, feel free to fork and submit a PR!

---

## 🧠 Author

Created by Javier J. Alvarez (https://github.com/Kiromentor/InsightPulse) — 2025  
Academic and learning project.
