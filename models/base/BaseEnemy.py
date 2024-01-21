from attrs import define, field

from .BaseEntity import BaseEntity

@define
class BaseEnemy(BaseEntity):
    assets_folder: str = 'assets/models/enemies'

