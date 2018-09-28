import random

from game_object import Object

class Player(Object):
    def __init__(self, width, height, pos_x, pos_y, image_url=None):
        super().__init__(width, height, pos_x, pos_y, image_url)

    def collision(self, enemy):
        pass


class Enemy(Object):
    def __init__(self, width, height, pos_x, pos_y, image_url=None):
        super().__init__(width, height, pos_x, pos_y, image_url)

    def reset_position(self, range):
        self.pos_x = random.randint(0, range-self.width)

