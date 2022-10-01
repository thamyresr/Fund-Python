import pygame
import random
import math

largura_tela = 800
altura_tela = 600

preto = (0, 0, 0)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

FPS = 5
lista_quadradinhos = []

pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
clock = pygame.time.Clock()

finalizar = False

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

    def desenhar_quadradinho(self, tela):
        pygame.draw.rect(tela, self.cor, self.area)

def desenhar_circulo(raio, posicao_x, posicao_y):
    pygame.draw.circle(tela, vermelho, (posicao_x, posicao_y), raio)
    fonte = pygame.font.Font(None, 24)
    texto = fonte.render("Clique", 1, branco)
    posicao_texto = (posicao_x - (raio // 2), posicao_y - 5)
    tela.blit(texto, posicao_texto)

circulo = desenhar_circulo(raio_circulo, posicao_x, posicao_y)

while not finalizar:
    verifica = True
    tela.fill(preto)
    for i in lista_quadradinhos:
        i.desenhar_quadradinho(tela)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizar = True
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            posicao_mouse = pygame.mouse.get_pos()
            distance = math.hypot(posicao_mouse[0] - posicao_x, posicao_mouse[1] - posicao_y)
            if distance <= raio_circulo:
                q = Quadradinho()
                q.desenhar_quadradinho(tela)
                for j in lista_quadradinhos:
                    if j.area.colliderect(q.area):
                        lista_quadradinhos.remove(j)
                        verifica = False
                if verifica:
                    lista_quadradinhos.append(q)

    circulo = desenhar_circulo(raio_circulo, posicao_x, posicao_y)
    pygame.display.update()

    clock.tick(FPS)

pygame.display.quit()
pygame.quit()
