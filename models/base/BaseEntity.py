from attrs import define, field

from models.base import BaseActor

@define
class BaseEntity(BaseActor):
    health: int
    damage: int
    armor: int
    resistance: int
    # min_stage: int
    # max_stage: int
    # welcome_phrases
    # bye_phrases
