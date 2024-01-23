import requests
import telebot
from telebot.types import InputFile, InputMediaPhoto, CallbackQuery

import os
from dotenv import load_dotenv

from game.game import get_game_state, start_game, handle_callback

load_dotenv()

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
# duncard, lostcard

bot = telebot.TeleBot(API_TOKEN)

def send_photo(chat_id, image_path, msg_text=None, markup=None):
    return bot.send_photo(chat_id, InputFile(image_path), msg_text, reply_markup=markup)
    # return bot.send_media_group(chat_id, [InputMediaPhoto(image_path, caption=text)])[0]
def edit_photo(chat_id, image_path, msg_id, msg_text=None, markup=None):
    return bot.edit_message_media(InputMediaPhoto(InputFile(image_path), caption=msg_text), chat_id, msg_id, reply_markup=markup)

def edit_photos_text(chat_id, msg_id, msg_text=None, markup=None):
    return bot.edit_message_caption(msg_text, chat_id, msg_id, reply_markup=markup)

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, "Добро пожаловать в подземелья! Введите /play, чтобы начать игру\n\nВнимание: это демо версия")

@bot.message_handler(commands=['play'])
def play_command(message):
    chat_id = message.chat.id
    state = get_game_state(chat_id)
    if state.is_running:
        bot.send_message(chat_id, "Игра уже идёт")
    else:
        start_game(state)

@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call: CallbackQuery):
    state = get_game_state(call.message.chat.id)
    if not state.is_running:
        bot.send_message(call.message.chat.id, "Попробуйте запустить новую игру с помощью /play")
    else:
        handle_callback(call, state)


@bot.message_handler(commands=['test'])
def test_command(message):
    bot.send_message(message.chat.id, "Hi there!")


@bot.message_handler(commands=['img'])
def send_image(message):
    # {'file_id': 'AgACAgIAAxkDAAIBomWe0FtuYFG1uKo2CsJWXxXvKPEeAALc0zEbzVX4SBVvFIxVNp4cAQADAgADcwADNAQ', 'file_unique_id': 'AQAD3NMxG81V-Eh4', 'width': 72, 'height': 90, 'file_size': 1591}
    msg = send_photo(message.chat.id, 'temp/poster.png', 'hello there what do you think of Marinette dupeng chang and miraculous ladybug?')
    photo = msg.photo[0]
    print(photo)
    print(msg.message_id)

def listener(messages):
    for m in messages:
        print(str(m))

print("Bot is running...")
# bot.set_update_listener(listener)
bot.infinity_polling()
