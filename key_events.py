class KeyEvent:
    def __init__(self, player):
        self.player = player
        self.moviment = 40

    def key_left(self):
        self.player.pos_x -= self.moviment

    def key_right(self):
        self.player.pos_x += self.moviment