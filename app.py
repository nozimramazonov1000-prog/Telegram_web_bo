import os
import threading
from flask import Flask
from dotenv import load_dotenv

from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
)

# .env ni yuklaymiz
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN topilmadi. .env yoki Render env ni tekshir!")

# ---------- FLASK ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "<h2>✅ Telegram Web Bot ishlayapti</h2>"


def run_flask():
    port = int(os.environ.get("PORT", 10000))  # Render uchun MUHIM
    app.run(host="0.0.0.0", port=port)


# ---------- TELEGRAM BOT ----------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom! Bot ishlayapti!")


def run_bot():
    application = (
        ApplicationBuilder()
        .token(BOT_TOKEN)
        .build()
    )

    application.add_handler(CommandHandler("start", start))

    application.run_polling(
        drop_pending_updates=True,
        close_loop=False
    )


# ---------- MAIN ----------
if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    run_flask()
