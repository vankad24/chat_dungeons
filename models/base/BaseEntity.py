from attrs import define, field

from models.base import BaseActor

@define
class BaseEntity(BaseActor):
    health: int
    damage: int
    armor: int
    # resistance: int
    # min_stage: int
    # max_stage: int
    # welcome_phrases
    # bye_phrases

    def attacked_by(self, attacker):
        ad = attacker.damage - self.armor
        if ad<0:
            ad = 0

        self.health-=ad
        return ad

    def is_alive(self):
        return self.health > 0
