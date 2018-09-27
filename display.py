import pygame

class DisplaySurface:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._size = (self.width, self.height)
        self._display_surface = pygame.display.set_mode(self._size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def get_display_surface(self):
        return self._display_surface

    def get_size(self):
        return self._size