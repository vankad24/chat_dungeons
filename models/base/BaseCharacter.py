from attrs import define, field

from .BaseEntity import BaseEntity

@define
class BaseCharacter(BaseEntity):
    assets_folder: str = 'assets/models/characters'
