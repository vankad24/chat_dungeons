from telebot.types import InputFile, InputMediaPhoto
from bot import bot
def send_photo(chat_id, image_path, msg_text=None, markup=None):
    return bot.send_photo(chat_id, InputFile(image_path), msg_text, reply_markup=markup)
    # return bot.send_media_group(chat_id, [InputMediaPhoto(image_path, caption=text)])[0]
def edit_photo(chat_id, image_path, msg_id, msg_text=None, markup=None):
    return bot.edit_message_media(InputMediaPhoto(InputFile(image_path), caption=msg_text), chat_id, msg_id, reply_markup=markup)

def edit_photos_text(chat_id, msg_id, msg_text=None, markup=None):
    return bot.edit_message_caption(msg_text, chat_id, msg_id, reply_markup=markup)
