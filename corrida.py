import os
import pygame 
import random
from objeto import Objeto

pygame.init() 

largura = 400 
altura = 600

vermelho = (255, 0, 0)
azul = (0, 0, 255)
verde = (0, 255, 0)

tela = pygame.display.set_mode((largura,altura))
pygame.display.set_caption("Meu primeiro jogo:| mentira, meu quinto jogo")

continuar = True

faixa_1 = Objeto(20, altura, 0, 0)
faixa_2 = Objeto(20, altura, largura-20, 0)
carro = Objeto(largura/4, altura/4, 3*largura/8, 3*altura/4)


while(continuar):
	for event in pygame.event.get():
		print(event.type)
		if(event.type == 12):
			continuar = False
		if(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_LEFT):
				carro.pos_x = carro.pos_x - 10
			elif(event.key == pygame.K_RIGHT):
				carro.pos_x = carro.pos_x + 10
	tela.fill(verde)
	faixa_1.draw(tela, azul)
	faixa_2.draw(tela, azul)
	carro.draw(tela, vermelho)
	pygame.display.update()

pygame.quit()


