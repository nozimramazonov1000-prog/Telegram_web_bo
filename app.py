from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def mini_app():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>Mini App</title>
        <style>
            body {
                font-family: Arial;
                background: #0f172a;
                color: white;
                text-align: center;
                padding: 40px;
            }
            .box {
                background: #1e293b;
                padding: 30px;
                border-radius: 20px;
            }
            button {
                margin-top: 20px;
                padding: 15px 25px;
                border: none;
                border-radius: 12px;
                background: #22c55e;
                color: black;
                font-size: 16px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h2>👋 Xush kelibsiz</h2>
            <p>Buyurtma berish uchun tayyormiz</p>
            <button>🛒 Buyurtma berish</button>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
