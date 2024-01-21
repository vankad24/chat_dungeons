from attrs import define, field
from PIL import Image
import os

@define
class BaseActor:
    texture = field(init=False)
    texture_filename: str = field(init=False)
    assets_folder: str = field(init=False)

    def __attrs_post_init__(self):
        self.texture = Image.open(os.path.join(self.assets_folder, self.texture_filename))
