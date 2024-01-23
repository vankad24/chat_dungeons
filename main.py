from bot import bot

# import bot commands handlers
from bot.commands import *

def listener(messages):
    for m in messages:
        print(str(m))

print("Bot is running...")
# bot.set_update_listener(listener)
bot.infinity_polling(timeout=123)
