from attrs import define, field

from models.base import BaseCharacter

@define
class Aria(BaseCharacter):
    texture_filename: str = 'aria.png'
    x_origin: int = 130
    max_health: int = 40
    damage: int = 5
    armor: int = 0
    resistance: int = 4