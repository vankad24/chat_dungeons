import telebot
import os
from dotenv import load_dotenv

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
# duncard, lostcard

bot = telebot.TeleBot(API_TOKEN)
