from attrs import define, field
from PIL import Image
import os

@define
class BaseActor:
    texture_filename: str = field(init=False)
    assets_folder: str = field(init=False)

    def get_image(self):
        return Image.open(os.path.join(self.assets_folder, self.texture_filename))
