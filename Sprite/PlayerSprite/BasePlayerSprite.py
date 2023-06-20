from Data.EventData import EventData
from Sprite.BaseSprite import BaseSprite


class BasePlayerSprite(BaseSprite):
    def __init__(self, x, y, image, name,blood, weapon):
        super().__init__(x, y, image, blood, weapon)
        self.name = name

    def update(self) -> None:
        if EventData.is_key_a_down:
            self.jump_up()
        if EventData.is_key_s_down:
            self.jump_below()
        if EventData.is_key_a_down:
            self.move_left()
        if EventData.is_key_d_down:
            self.move_right()