from telebot.types import CallbackQuery

from bot.functions import send_photo
from main import bot
from game.game import get_game_state, start_game, handle_callback


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


@bot.callback_query_handler(func=lambda call: True)
def handle_button_click(call: CallbackQuery):
    state = get_game_state(call.message.chat.id)
    if not state.is_running:
        bot.send_message(call.message.chat.id, "Попробуйте запустить новую игру с помощью /play")
    else:
        handle_callback(call, state)

