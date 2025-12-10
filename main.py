import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
genai.configure(api_key=GEMINI_API_KEY)

@bot.message_handler(func=lambda msg: True)
def reply(message):
    user_text = message.text
    try:
        response = genai.chat.completions.create(
            model="gemini-pro",
            messages=[{"role": "user", "content": user_text}]
        )
        bot.send_message(message.chat.id, response.choices[0].message.content)
    except Exception as e:
        bot.send_message(message.chat.id, f"Ошибка: {e}")

bot.polling(none_stop=True)
