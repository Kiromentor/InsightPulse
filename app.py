from flask import Flask, render_template, request
from analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    text = ""
    language = "en"
    if request.method == "POST":
        text = request.form["text"]
        language = request.form["language"]
        result = analyze_text(text, language)
    return render_template("index.html", result=result, text=text, language=language)

# Solo para local, pero innecesario para Render
# if __name__ == "__main__":
#     app.run(debug=True)
