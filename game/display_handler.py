import os
import time
from PIL import Image, ImageDraw, ImageFont

from models.base import BaseEnemy, BaseStage, BaseCharacter

TEMP_FOLDER = 'temp'

if not os.path.exists(TEMP_FOLDER):
    os.makedirs(TEMP_FOLDER)

font = ImageFont.truetype('assets/fonts/better-vcr.ttf', 24)


def draw_health_bar(drawable: ImageDraw, center_x, y, current_hp, max_hp):
    hp_percent = current_hp/max_hp
    fill_color = '#ed3030'
    background_color = '#4f4a55'
    outline_color = '#312a3a'
    outline_width = 2
    bar_y_offset = 35
    bar_height = 18
    bar_width = 300
    hp_margin = 10

    y1 = y-bar_y_offset
    y2 = y1+bar_height
    center_x-= bar_width // 2
    drawable.rectangle([center_x, y1 - outline_width, center_x + bar_width, y2 + outline_width], fill=background_color, outline=outline_color, width=outline_width)
    drawable.rectangle([center_x + outline_width, y1, center_x + bar_width * hp_percent - outline_width, y2], fill=fill_color)
    drawable.text((center_x + bar_width + hp_margin, y1), str(current_hp), font=font, fill=fill_color, align="left", stroke_fill=outline_color, stroke_width=outline_width)


def create_game_image(stage: BaseStage, character: BaseCharacter, enemy: BaseEnemy):
    background = stage.get_image()
    char_img = character.get_image()
    enemy_img = enemy.get_image()

    char_x, char_y = stage.character_x_center, stage.character_y_bottom
    char_x -= character.x_origin
    char_y -= char_img.height
    background.paste(char_img, (char_x, char_y), char_img)

    enemy_x, enemy_y = stage.enemy_x_center, stage.enemy_y_bottom
    enemy_x -= enemy.x_origin
    enemy_y -= enemy_img.height
    background.paste(enemy_img, (enemy_x, enemy_y), enemy_img)

    # Create a drawing object
    draw = ImageDraw.Draw(background)

    draw_health_bar(draw, stage.character_x_center, char_y, character.health, character.max_health)
    draw_health_bar(draw, stage.enemy_x_center, enemy_y, enemy.health, enemy.max_health)


    image_path = os.path.join(TEMP_FOLDER, str(int(time.time()*1000))+'.png')
    background.save(image_path)

    background.close()
    char_img.close()
    enemy_img.close()

    return image_path