import pygame

class Objeto():
	def __init__(self, largura, comprimento, pos_x, pos_y, image_url = None):
		if image_url:
			self.image_surface = pygame.image.load(image_url)

		self.image_url = image_url
		self.largura = largura
		self.comprimento = comprimento
		self.pos_x = pos_x
		self.pos_y = pos_y

	def scale_image(self):
		self.image_surface = pygame.transform.scale(self.image_surface, (self.largura, self.comprimento))

	def draw(self, surface, cor):
		pygame.draw.rect(surface, cor, self.get_pos()+self.get_size())

	def get_pos(self):
		return [self.pos_x, self.pos_y]

	def get_size(self):
		return [self.largura, self.comprimento]

	def get_image_surface(self):
		return self.image_surface
