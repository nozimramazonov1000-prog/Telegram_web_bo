import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# =====================
# TELEGRAM BOT TOKEN
# =====================
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# =====================
# FLASK APP
# =====================
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Telegram Bot ishlayapti!"

# =====================
# TELEGRAM BOT HANDLERS
# =====================
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salom! Bot ishlayapti ✅")

def run_bot():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling(drop_pending_updates=True)

# =====================
# MAIN
# =====================
if __name__ == "__main__":
    # Telegram botni alohida oqimda ishga tushiramiz
    threading.Thread(target=run_bot).start()

    # Flask PORT (Render uchun MUHIM)
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
