import os
import telebot
import google.generativeai as genai

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

bot = telebot.TeleBot(8590221607:AAGo4jKRjAZR6UtiKEfuZKsBY2BN29CthcY)

genai.configure(api_key=AIzaSyD4gHcU51Txs1rIL3a3oMb6TDQkedm-5hc)

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
