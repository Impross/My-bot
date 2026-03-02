import telebot
from flask import Flask
import threading
import os

# သင်၏ Telegram Token
TOKEN = '8727032305:AAHhjlbareNK2-v6vt2l_gf-0rKKwupIrvg'
bot = telebot.TeleBot(TOKEN)

app = Flask('')

@app.route('/')
def home():
    return "Bot is running 24/7 on Render!"

def run_flask():
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

@bot.message_handler(func=lambda message: True)
def reply_message(message):
    text = message.text.lower()
    if "မင်္ဂလာပါ" in text:
        bot.reply_to(message, "မင်္ဂလာပါခင်ဗျာ။၂၄ နာရီ စာပြန်ပေးနေပါတယ်!")
    elif "နေကောင်းလား" in text:
        bot.reply_to(message, "နေကောင်းပါတယ်ခင်ဗျ။ လူကြီးမင်းရော?")
    else:
        bot.reply_to(message, "ကျွန်တော်က၂၄ နာရီ ရှိနေမယ့် Bot လေးပါ။")

if __name__ == "__main__":
    t = threading.Thread(target=run_flask)
    t.start()
    print("Bot is starting on Cloud...")
    bot.polling()
  
