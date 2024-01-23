from attrs import define, field

from models.base import BaseCharacter

@define
class Viren(BaseCharacter):
    texture_filename: str = 'viren.png'
    x_origin: int = 220
    max_health: int = 40
    damage: int = 5
    armor: int = 0
    resistance: int = 3