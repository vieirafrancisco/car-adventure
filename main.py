import os
import random

import pygame
from pygame.locals import *

from objeto import Objeto
from carros import Player, Enemy
from key_events import KeyEvent
from display import DisplaySurface

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
        self.size = self.width, self.height = 480, 640

        self.faixa = Objeto(10, self.height, (self.width/2)-5, 0)
        
        # Player object
        self.carro = Player(80, 120, 80, self.height-120, os.path.join("image", "carro.png"))
        self.carro.scale_image()
        
        # Enemy object
        self.enemy = Enemy(80, 120, random.randint(0, self.width), 0, os.path.join("image", "inimigo.png"))
        self.enemy.scale_image()
        self.enemy.rotate_image(angle=180)

        # Key event
        self.car_key = None

        # Clock
        self.clock = pygame.time.Clock()

    def on_init(self):
        pygame.init()
        self._display_surf = DisplaySurface(self.width, self.height)
        pygame.display.set_caption(self.title)
        self.car_key = KeyEvent(self._display_surf, self.carro)
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pygame.display.update()

    def on_render(self):
        self._display_surf.get_display_surface().fill(cores["cinza"])
        self.faixa.draw(self._display_surf.get_display_surface(), cores["branco"])
        self._display_surf.get_display_surface().blit(self.carro.get_image_surface(), self.carro.get_pos())
        self._display_surf.get_display_surface().blit(self.enemy.get_image_surface(), self.enemy.get_pos())
        
        if(self.enemy.pos_y >= self.height):
            self.enemy.pos_y = 0
            self.enemy.reset_position(range=self.width)
        else:
            self.enemy.pos_y += 10

        self.clock.tick(30)

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        if(self.on_init() == False):
            self._running = False

        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)

                # Key press button
                if event.type == pygame.KEYDOWN:

                    # Left click button
                    if event.key == pygame.K_LEFT:
                        self.car_key.key_left()

                    # Right click button
                    if event.key == pygame.K_RIGHT:
                        self.car_key.key_right()

            self.on_loop()
            self.on_render()
        self.on_cleanup()

if __name__ == '__main__':
    app = App("Car Adventure")
    app.on_execute()