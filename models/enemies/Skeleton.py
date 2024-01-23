from attrs import define, field

from models.base import BaseEnemy


@define
class Skeleton(BaseEnemy):
    texture_filename: str = 'skeleton.png'
    x_origin: int = 208
    max_health: int = 20
    damage: int = 3
    armor: int = 0
    resistance: int = 0

