from flask import Flask, request
import os

app = Flask(__name__)

# === TEST UCHUN MAHSULOTLAR (keyin DB qilamiz) ===
products = [
    {
        "name": "Creative Headphones",
        "price": "250 000 so'm",
        "desc": "Yuqori sifatli ovoz va zamonaviy dizayn",
        "img": "https://via.placeholder.com/300"
    },
    {
        "name": "Smart Watch",
        "price": "480 000 so'm",
        "desc": "Sport va kundalik hayot uchun",
        "img": "https://via.placeholder.com/300"
    },
    {
        "name": "Wireless Speaker",
        "price": "320 000 so'm",
        "desc": "Kuchli bass va tiniq ovoz",
        "img": "https://via.placeholder.com/300"
    }
]

# === WEB SAHIFA ===
@app.route("/")
def index():
    html = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Creative Online Shop</title>
        <style>
            body {
                font-family: Arial;
                background: linear-gradient(120deg, #f6d365, #fda085);
                margin: 0;
                padding: 20px;
            }
            h1 {
                text-align: center;
                color: #fff;
            }
            .container {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 20px;
                margin-top: 30px;
            }
            .card {
                background: #fff;
                border-radius: 15px;
                padding: 15px;
                box-shadow: 0 10px 20px rgba(0,0,0,0.2);
                text-align: center;
            }
            .card img {
                width: 100%;
                border-radius: 10px;
            }
            .price {
                color: green;
                font-weight: bold;
                margin-top: 10px;
            }
        </style>
    </head>
    <body>
        <h1>🛍 Creative Online Shop</h1>
        <div class="container">
    """

    for p in products:
        html += f"""
        <div class="card">
            <img src="{p['img']}">
            <h3>{p['name']}</h3>
            <p>{p['desc']}</p>
            <div class="price">{p['price']}</div>
        </div>
        """

    html += """
        </div>
    </body>
    </html>
    """
    return html


# === TELEGRAM BOTDAN TEST UCHUN ===
@app.route("/bot", methods=["POST"])
def bot_javobi():
    data = request.json
    text = data.get("text", "")

    if text.lower() == "salom":
        return {"reply": "Salom 👋 Online do‘konimizga xush kelibsiz!"}

    return {"reply": "Mahsulotlarni ko‘rish uchun web sahifani oching 🛍"}


# === RENDER UCHUN MUHIM QISM ===
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
