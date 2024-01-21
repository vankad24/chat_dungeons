from attrs import define, field

from models.base import BaseCharacter

@define
class Aria(BaseCharacter):
    texture_filename: str = 'aria.png'
    health = 40
    damage = 5