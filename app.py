import os
from flask import Flask
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

TOKEN = os.getenv("BOT_TOKEN")

app = Flask(__name__)

# Telegram bot
bot_app = Application.builder().token(TOKEN).build()


# ===== BOT BUYRUQLARI =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Salom! Bot ishlayapti.")


bot_app.add_handler(CommandHandler("start", start))


# ===== FLASK ROUTE =====
@app.route("/")
def home():
    return "✅ Bot server ishlayapti"


# ===== ASOSIY ISHGA TUSHISH =====
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))

    # botni backgroundda ishga tushiramiz
    bot_app.run_polling(stop_signals=None)

    # Flask server (Render portni ko‘radi)
    app.run(host="0.0.0.0", port=port)
