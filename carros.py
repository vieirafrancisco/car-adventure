from objeto import Objeto

class Player(Objeto):
    def __init__(self, width, height, pos_x, pos_y, image_url=None):
        super().__init__(width, height, pos_x, pos_y, image_url)


class Enemy(Objeto):
    def __init__(self, width, height, pos_x, pos_y, image_url=None):
        super().__init__(width, height, pos_x, pos_y, image_url)

    def reset_position(self):
        pass

