from attrs import define, field

from models.base import BaseActor


@define
class BaseStage(BaseActor):
    assets_folder: str = 'assets/models/stages'


