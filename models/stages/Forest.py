from attrs import define, field

from models.base import BaseStage


@define
class Forest(BaseStage):
    texture_filename: str = 'forest.png'
    character_x_center: int = 220
    character_y_bottom: int = 915
    enemy_x_center: int = 800
    enemy_y_bottom: int = 920