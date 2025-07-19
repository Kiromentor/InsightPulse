from flask import Flask, render_template, request
from analyzer import analyze_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        text = request.form["text"]
        result = analyze_text(text)
    return render_template("index.html", result=result)

# Solo para local, pero innecesario para Render
# if __name__ == "__main__":
#     app.run(debug=True)
