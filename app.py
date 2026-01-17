import os
from telebot import TeleBot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton, WebAppInfo

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = TeleBot(BOT_TOKEN)

# /start komandasi
@bot.message_handler(commands=['start'])
def start(message):
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(
        KeyboardButton(
            "🧩 Mini App ochish",
            web_app=WebAppInfo(
                url="https://telegram-web-bo-2234.onrender.com"
            )
        )
    )

    bot.send_message(
        message.chat.id,
        "Mini Web App’ni ochish uchun tugmani bosing 👇",
        reply_markup=markup
    )

# Mini Web App’dan kelgan datani ushlash
@bot.message_handler(content_types=['web_app_data'])
def web_app_handler(message):
    data = message.web_app_data.data
    bot.send_message(
        message.chat.id,
        f"✅ Mini App’dan keldi:\n{data}"
    )

if __name__ == "__main__":
    bot.infinity_polling()
