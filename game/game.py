from enum import Enum

from attrs import define, field
from telebot.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton

from game.display_handler import create_game_image
from bot.functions import send_photo, edit_photo, edit_photos_text
from bot import bot
from models.base import BaseStage, BaseCharacter, BaseEnemy
from models.characters.Viren import Viren
from models.characters.Aria import Aria
from models.enemies.Skeleton import Skeleton
from models.stages.Forest import Forest

from random import randint

game_states = {}

class Phase(Enum):
    WELCOME = 1
    CHOSE_ACTION = 2
    END = 3

@define
class CallbackAction:
    NEXT = 'next'
    ATTACK = 'attack'
    FINISH = 'finish'

@define
class GameState:
    user_id: int = field(init=True)
    current_msg_id: int = field(init=False)
    stage: BaseStage = field(init=False)
    character: BaseCharacter = field(init=False)
    enemy: BaseEnemy = field(init=False)
    current_phase = field(init=False, default=Phase.WELCOME)
    is_running: bool = field(init=False, default=False)
    reply_message: str = field(init=False, default='')

    def add_message(self, msg):
        self.reply_message+=msg+'\n'

    def clear_message(self):
        self.reply_message = ''

    def get_image_path(self):
        return create_game_image(self.stage, self.character, self.enemy)

    def get_markup(self):
        keyboard = InlineKeyboardMarkup()
        match self.current_phase:
            case Phase.WELCOME:
                button = InlineKeyboardButton("Продолжить", callback_data=CallbackAction.NEXT)
                keyboard.row(button)
            case Phase.CHOSE_ACTION:
                button = InlineKeyboardButton("Атаковать", callback_data=CallbackAction.ATTACK)
                keyboard.row(button)
            case Phase.END:
                button = InlineKeyboardButton("Продолжить", callback_data=CallbackAction.FINISH)
                keyboard.row(button)
            case _:
                keyboard = None
        return keyboard

    def battle(self):
        e = self.enemy
        c = self.character
        damage = e.attacked_by(c)
        self.add_message(f"Вы нанесли {damage} урона")
        if e.is_alive():
            damage = c.attacked_by(e)
            self.add_message(f"Враг атаковал в ответ и нанёс {damage} урона")

            if not c.is_alive():
                self.add_message(f"Вы не выдержали такого удара")

        else:
            self.add_message(f"Враг был повержен столь сокрушающей силой")



def get_game_state(user_id):
    # todo add game id
    if user_id in game_states:
        return game_states[user_id]
    state = GameState(user_id)
    game_states[user_id] = state
    return state

def start_game(state: GameState):
    state.is_running = True
    state.current_phase = Phase.WELCOME
    state.enemy = Skeleton()
    state.stage = Forest()
    state.character = Viren()
    load_msg = bot.send_message(state.user_id, "Загрузка...")
    msg = send_photo(state.user_id, state.stage.assets_folder+"/"+state.stage.texture_filename, "Вирен шёл по прекрасной поляне, как вдруг встретил скелета", state.get_markup())
    bot.delete_message(state.user_id, load_msg.message_id)
    state.current_msg_id = msg.message_id
    state.clear_message()

def handle_callback(call: CallbackQuery, state: GameState):

    match call.data:
        case CallbackAction.NEXT:
            if state.current_phase == Phase.WELCOME:
                state.current_phase = Phase.CHOSE_ACTION
                state.add_message("Что ж, надирём им задницу!")
        case CallbackAction.ATTACK:
            state.battle()
            if not state.enemy.is_alive() or not state.character.is_alive():
                state.current_phase = Phase.END
        case CallbackAction.FINISH:
            state.is_running = False
            edit_photo(state.user_id, state.stage.assets_folder+"/"+state.stage.texture_filename, state.current_msg_id, "Вирен смачно ушёл в закат...")
            return

    update_game_message(state)

def update_game_message(state):

    edit_photos_text(state.user_id, state.current_msg_id, "Загрузка...")

    edit_photo(state.user_id, state.get_image_path(), state.current_msg_id, state.reply_message, state.get_markup())

    state.clear_message()

