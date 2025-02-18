import telebot
import os
from flask import Flask, request

# הגדרות בסיסיות
BOT_TOKEN = '7668567141:AAHvAdau0XysVELfdS3XMuKUS_354CHWuZ4'
bot = telebot.TeleBot(BOT_TOKEN)

# יצירת אפליקציית Flask
app = Flask(__name__)

# טיפול בפקודת /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "שלום! אני בוט חדש. איך אני יכול לעזור?")

# טיפול בהודעות טקסט
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.reply_to(message, f"קיבלתי את ההודעה שלך: {message.text}")

# הגדרת ה-webhook
@app.route(f'/{BOT_TOKEN}', methods=['POST'])
def webhook():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return 'OK'

# דף הבית פשוט
@app.route('/')
def home():
    return 'הבוט פעיל!'

# הפעלת השרת
if __name__ == '__main__':
    app.run()
