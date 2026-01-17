import os
import threading
from flask import Flask, render_template
from dotenv import load_dotenv

from telegram import Update, WebAppInfo, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
WEB_URL = os.getenv("WEB_URL")  # Render URL

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi (.env ni tekshir)")

app = Flask(__name__)

# ---------- FLASK ----------
@app.route("/")
def index():
    return render_template("index.html")

# ---------- TELEGRAM BOT ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            KeyboardButton(
                "📦 Buyurtma berish",
                web_app=WebAppInfo(url=WEB_URL)
            )
        ]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Xush kelibsiz!", reply_markup=reply_markup)

async def web_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.effective_message.web_app_data.data
    await update.message.reply_text(f"✅ Buyurtma qabul qilindi: {data}")

def run_bot():
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters.StatusUpdate.WEB_APP_DATA, web_data)
    )

    application.run_polling(drop_pending_updates=True)

# ---------- RUN ----------
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    app.run(host="0.0.0.0", port=10000)
