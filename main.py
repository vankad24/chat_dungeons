import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
# duncard, lostcard

bot = telebot.TeleBot(API_TOKEN)

# import bot commands handlers
from bot.commands import *

def listener(messages):
    for m in messages:
        print(str(m))

print("Bot is running...")
# bot.set_update_listener(listener)
bot.infinity_polling()
