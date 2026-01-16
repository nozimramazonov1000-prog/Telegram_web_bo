from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    javob = ""
    if request.method == "POST":
        javob = request.form.get("text")
    return f"""
    <html>
    <body>
        <h2>Mini Web Bot</h2>
        <form method="post">
            <input name="text" placeholder="Matn yozing">
            <button type="submit">Yuborish</button>
        </form>
        <p>{javob}</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
