import pygame
from pygame.locals import *
import random

largura_tela = 800
altura_tela = 600

preto = (0, 0, 0)
branco = (255, 255, 255)

FPS = 60
lista_quadrados = []

pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()
finalizar = False

class Quadradinho():

    def __init__(self):
        self.largura = 50
        self.altura = 50
        self.x = random.randint(0, largura_tela - self.largura)
        self.y = random.randint(0, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (255, 255, 0)

    def desenhar_quadrado(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

while not finalizar:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizar = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            desenho = Quadradinho()
            lista_quadrados.append(desenho)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_SPACE:
                desenho = Quadradinho()
                lista_quadrados.append(desenho)
    tela.fill(preto)
    for i in lista_quadrados:
        i.desenhar_quadrado(tela)

    pygame.display.update()

    clock.tick(FPS)

pygame.display.quit()
pygame.quit()
