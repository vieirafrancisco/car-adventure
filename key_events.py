class KeyEvent:
    def __init__(self, display, player):
        self._display = display
        self.player = player
        self.moviment = 40

    def key_left(self):
        if self.player.pos_x - 40 >= 0:
            self.player.pos_x -= self.moviment

    def key_right(self):
        if self.player.pos_x + 40 <= self._display.width-80:
            self.player.pos_x += self.moviment