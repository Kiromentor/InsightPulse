# InsightPulse 🧠✨

Análisis de sentimiento y extracción de palabras clave con Flask + TextBlob + NLTK

---

## 📌 ¿Qué es InsightPulse?

**InsightPulse** es una aplicación web simple pero poderosa que permite analizar texto ingresado por el usuario para:

* Detectar el **sentimiento** (polaridad: positivo, negativo o neutro)
* Extraer **palabras clave** significativas (sustantivos o frases clave)

Está construida con Python, Flask y utiliza bibliotecas de procesamiento de lenguaje natural (NLP) como **TextBlob** y **NLTK**.

---

## 🚀 ¿Para qué sirve?

Este proyecto es ideal para:

* Entrenarse con procesamiento de texto en Python
* Entender conceptos básicos de NLP
* Crear una app web con análisis en tiempo real
* Mostrar en tu portafolio como ejemplo práctico

---

## 🧰 Tecnologías utilizadas

* Python 3.13+
* Flask
* TextBlob
* NLTK
* HTML + TailwindCSS (CDN)
* Render (para deploy gratuito)

---

## 📷 Captura de pantalla

*Agregá una captura o GIF del proyecto funcionando aquí*

---

## ⚙️ Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git clone https://github.com/Kiromentor/InsightPulse
cd insightpulse
```

### 2. Crear entorno virtual e instalar dependencias

```bash
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Descargar datos de NLTK y TextBlob

```python
# En Python interactivo
import nltk
nltk.download('punkt')
nltk.download('brown')

# O usar:
python -m textblob.download_corpora
```

### 4. Ejecutar la app

```bash
flask run
```

---

## 🌐 Deploy en Render

Render requiere:

* `requirements.txt`
* `app.py`
* archivo `render.yaml` (opcional)
* uso de `gunicorn` como comando de arranque (`gunicorn app:app`)

---

## 🤝 Contribuciones

¡Son bienvenidas! Si querés mejorar la interfaz, agregar nuevos análisis o integrar APIs externas, ¡hacé un fork y mandá un PR!

---

## 🧠 Autor

Creado por Javier J. Alvarez (https://github.com/Kiromentor/InsightPulse) — 2025
Proyecto académico y de aprendizaje.
