# app.py
from flask import Flask, render_template, request
from analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""
    selected_lang = "en"  # Valor por defecto
    if request.method == "POST":
        text = request.form.get("text", "").strip()
        selected_lang = request.form.get("lang", "en")

        if not text:
            return "Missing text input", 400

        result = analyze_text(text, lang=selected_lang)

    return render_template("index.html", result=result, text=text, selected_lang=selected_lang)

# Solo para local, pero innecesario para Render
# if __name__ == "__main__":
#     app.run(debug=True)
