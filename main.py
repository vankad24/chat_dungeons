import requests
import telebot
from telebot import types
# pip install pyTelegramBotAPI
from telebot.types import InputFile
import time
import os
from dotenv import load_dotenv
load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')

bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в подземелья!")

@bot.message_handler(commands=['play'])
def play_command(message):
    ...

@bot.message_handler(commands=['test'])
def test_command(message):
    time.sleep(3)
    bot.send_message(message.chat.id, "Hi there!")

@bot.message_handler(commands=['message'])
def send_message_with_keyboard(message):
    # Создаем клавиатуру с кнопками
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    repeat_button = types.InlineKeyboardButton("Повторить", callback_data='repeat')
    ok_button = types.InlineKeyboardButton("Нет", callback_data='no')
    keyboard.add(repeat_button, row_width=2)
    keyboard.add(ok_button, row_width=1)


    # Отправляем сообщение с кнопками
    bot.send_message(message.chat.id, "Привет! ", reply_markup=keyboard)


# func - filter function. Call Obfect fields https://pytba.readthedocs.io/en/latest/types.html#telebot.types.CallbackQuery
@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call):
    if call.data == 'repeat':
        # Отправляем сообщение повторно
        # bot.send_message(call.message.chat.id, "Привет!", reply_markup=call.message.reply_markup)
        send_message_with_keyboard(call.message)
    elif call.data == 'no':
        message = call.message
        # Меняем сообщение
        bot.edit_message_text('Я тебя прекрасно понимаю, брат!', message.chat.id, message.message_id)
        # Меняем кнопки. Добавляем ссылку на легендарную песню
        keyboard = types.InlineKeyboardMarkup()
        link_button = types.InlineKeyboardButton("Для успокоения", url="https://youtu.be/dQw4w9WgXcQ")
        keyboard.add(link_button)
        bot.edit_message_reply_markup(message.chat.id, message.message_id, reply_markup=keyboard)

@bot.message_handler(commands=['img'])
def send_image(message):
    # msg = bot.send_photo(message.chat.id, InputFile('tests/poster.png'))
    # {'file_id': 'AgACAgIAAxkDAAIBomWe0FtuYFG1uKo2CsJWXxXvKPEeAALc0zEbzVX4SBVvFIxVNp4cAQADAgADcwADNAQ', 'file_unique_id': 'AQAD3NMxG81V-Eh4', 'width': 72, 'height': 90, 'file_size': 1591}
    msg = bot.send_photo(message.chat.id, "AgACAgIAAxkDAAIBomWe0FtuYFG1uKo2CsJWXxXvKPEeAALc0zEbzVX4SBVvFIxVNp4cAQADAgADcwADNAQ")
    photo = msg.photo[0]
    print(photo)
    print(photo.file_id)


print("Bot is running...")
bot.infinity_polling()
