from attrs import define, field

from models.base import BaseStage


@define
class PeacefulStage(BaseStage):
    texture_filename: str = 'peaceful.png'