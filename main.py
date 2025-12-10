import os
import logging
import telebot
import google.generativeai as genai

# Logging
logging.basicConfig(level=logging.INFO)

# Keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# Set up Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-pro")

@bot.message_handler(func=lambda msg: True)
def reply(message):
    user_text = message.text
    response = model.generate_content(user_text)
    bot.send_message(message.chat.id, response.text)

bot.polling(none_stop=True)
