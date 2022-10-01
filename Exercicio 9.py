import pygame
from pygame.locals import *
import random
import math

largura_tela = 800
altura_tela = 600

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

FPS = 50
lista_quadradinhos = []

pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()

finalizado = False

raio_circulo = 50
posicao_x = largura_tela // 2
posicao_y = raio_circulo
area = (posicao_x, posicao_y)

class Quadradinho():
    def __init__(self):
        self.largura = 50
        self.altura = 40
        self.x = random.randint(0, largura_tela - self.largura)
        self.y = random.randint(0, altura_tela - self.altura)
        self.area = pygame.Rect(self.x, self.y, self.largura, self.altura)
        self.cor = (255, 255, 0)

    def desenhar_quadrado(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

def desenhar_circulo(raio, xpos, ypos):
    pygame.draw.circle(tela, vermelho, (xpos, ypos), raio)
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render("Clique", 1, branco)
    posicao_texto = (xpos - (raio // 2), ypos - 5)
    tela.blit(texto, posicao_texto)

def colisao(rleft, rtop, width, height, center_x, center_y, radius):
    rright, rbottom = rleft + width / 2, rtop + height / 2

    cleft, ctop = center_x - radius, center_y - radius
    cright, cbottom = center_x + radius, center_y + radius

    if rright < cleft or rleft > cright or rbottom < ctop or rtop > cbottom:
        return False

    for x in (rleft, rleft + width):
        for y in (rtop, rtop + height):
            if math.hypot(x - center_x, y - center_y) <= radius:
                return True

    if rleft <= center_x <= rright and rtop <= center_y <= rbottom:
        return True
    return False

circulo = desenhar_circulo(raio_circulo, posicao_x, posicao_y)

pygame.key.set_repeat(50, 50)

while not finalizado:
    verificacao = True
    tela.fill(preto)
    for i in lista_quadradinhos:
        i.desenhar_quadrado(tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizado = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()
            distancia = math.hypot(posicao_mouse[0] - posicao_x, posicao_mouse[1] - posicao_y)
            if distancia <= raio_circulo:
                q = Quadradinho()
                q.desenhar_quadrado(tela)
                for j in lista_quadradinhos:
                    if j.area.colliderect(q.area):
                        lista_quadradinhos.remove(j)
                        verificacao = False
                if verificacao:
                    lista_quadradinhos.append(q)

        tecla_pressionada = pygame.key.get_pressed()

        if tecla_pressionada[K_w]:
            posicao_y -= 5
        elif tecla_pressionada[K_s]:
            posicao_y += 5
        elif tecla_pressionada[K_a]:
            posicao_x -= 5
        elif tecla_pressionada[K_d]:
            posicao_x += 5

    circulo = desenhar_circulo(raio_circulo, posicao_x, posicao_y)

    for i in lista_quadradinhos:
        if colisao(i.area.left, i.area.top, i.largura, i.altura, posicao_x, posicao_y, raio_circulo):
            lista_quadradinhos.remove(i)

    pygame.display.update()
    clock.tick(FPS)

pygame.display.quit()
pygame.quit()
