import os
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    javob = ""
    if request.method == "POST":
        javob = request.form.get("text", "")
    return f"""
    <html>
    <head>
        <title>Mini Web Do‘kon</title>
        <style>
            body {{
                font-family: Arial;
                background: #f2f2f2;
                padding: 30px;
            }}
            .card {{
                background: white;
                padding: 20px;
                border-radius: 10px;
                width: 300px;
            }}
        </style>
    </head>
    <body>
        <h2>🛒 Mini Web Do‘kon</h2>
        <div class="card">
            <form method="post">
                <input name="text" placeholder="Matn yozing">
                <button type="submit">Yuborish</button>
            </form>
            <p>{javob}</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
