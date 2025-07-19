# InsightPulse 🧠✨

Análisis de sentimiento y extracción de palabras clave con Flask + TextBlob + NLTK

---

## 📌 ¿Qué es InsightPulse?

**InsightPulse** es una aplicación web simple pero poderosa que permite analizar texto ingresado por el usuario para:

* Detectar el **sentimiento** (polaridad: positivo, negativo o neutro)
* Extraer **palabras clave** significativas (sustantivos o frases clave)
* Visualizar un **mapa de palabras** (word cloud) con tamaños según relevancia

Está construida con Python, Flask y utiliza bibliotecas de procesamiento de lenguaje natural (NLP) como **TextBlob** y **NLTK**.

---

## 🚀 ¿Para qué sirve?

Este proyecto es ideal para:

* Practicar procesamiento de texto en Python
* Entender conceptos básicos de NLP
* Crear una app web interactiva
* Mostrarlo como proyecto de portafolio personal

---

## 🧰 Tecnologías utilizadas

* Python 3.10+
* Flask
* TextBlob
* NLTK
* WordCloud
* Matplotlib
* HTML + TailwindCSS (CDN)
* Replit (para ejecutar gratis en la nube)

---

## 📷 Captura de pantalla

> Agregá una captura o GIF del proyecto funcionando aquí  
> Ejemplo: `static/wordcloud.png` o una imagen del resultado del análisis

---

## ⚙️ Cómo ejecutar el proyecto en Replit

1. **Importar repositorio o subir archivos en Replit**

2. **Instalar dependencias** (en el shell o en el archivo `replit.nix`):

```bash
pip install -r requirements.txt
```

3. **Descargar los datos de NLTK (una sola vez)**

```python
# Desde el shell interactivo de Python
import nltk
nltk.download('punkt')
nltk.download('brown')
```

4. **Ejecutar la app**

```bash
python app.py
```

Y accedé a la URL generada por Replit.

---

## 🌍 Cómo funciona

El usuario escribe un texto en inglés o español, selecciona el idioma y presiona "Analyze".  
La app detecta el sentimiento usando **TextBlob** y extrae palabras clave.  
Luego genera una **nube de palabras estática** donde las palabras más importantes se ven más grandes.

---

## 🤝 Contribuciones

¡Son bienvenidas! Si querés mejorar la interfaz, agregar nuevos análisis o integrar APIs externas, ¡hacé un fork y mandá un PR!

---

## 🧠 Autor

Creado por Javier J. Alvarez  
🔗 https://github.com/Kiromentor/InsightPulse  
📅 Año: 2025 — Proyecto académico y de aprendizaje
