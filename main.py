import os

import pygame
from pygame.locals import *

from objeto import Objeto
from key_events import KeyEvent

cores = {
    "vermelho": (255,0,0),
    "verde": (0, 255, 0),
    "azul": (0,0,255),
    "cinza": (168, 168, 168),
    "branco": (255, 255, 255)
}

class App:
    def __init__(self, title=None):
        if title:
            self.title = title
        else:
            self.title = "New Game"

        self._running = True
        self._display_surf = None
        self.size = self.weight, self.height = 480, 640

        self.faixa = Objeto(10, self.height, (self.weight/2)-5, 0)
        self.carro = Objeto(80, 120, 80, self.height-120, os.path.join("image", "carro.png"))
        self.carro.scale_image()

        # Key event
        self.car_key = KeyEvent(self.carro)

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        pygame.display.set_caption(self.title)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.display.update()

    def on_render(self):
        self._display_surf.fill(cores["cinza"])
        self.faixa.draw(self._display_surf, cores["branco"])
        self._display_surf.blit(self.carro.get_image_surface(), self.carro.get_pos())

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if(self.on_init() == False):
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if self.carro.pos_x - 40 >= 0:
                            self.car_key.key_left()
                    if event.key == pygame.K_RIGHT:
                        if self.carro.pos_x + 40 <= self.weight-80:
                            self.car_key.key_right()
            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__':
    app = App("Car Adventure")
    app.on_execute()