from attrs import define, field

from models.base import BaseActor

# stage default resolution is 1024x1024
# start_x - where will be an entity texture center
# start_y - where will be bottom y of an entity texture
@define
class BaseStage(BaseActor):
    character_x_center: int
    character_y_bottom: int
    enemy_x_center: int
    enemy_y_bottom: int
    assets_folder: str = 'assets/models/stages'


