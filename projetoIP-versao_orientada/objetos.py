import pygame
from random import randint
from player import *

class Objetos():

    def __init__(self, tamanho, valor, img, pos_x=randint(0,836), pos_y=0, aux = 0):
        self.tamanho = tamanho
        self.valor = valor
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        self.img = pygame.image.load(img).convert_alpha()

    def cair(self, janela, velocidade):
        self.pos_y += velocidade + 5
        janela.blit(self.img, (self.pos_x, self.pos_y))

    def colisao(self, player_x, player_y):
        valor = -1
        if player_y - 32 <= self.pos_y <= player_y + 32 and player_x - 32 <= self.pos_x <= player_x + 32:
            valor = self.valor
            # Efeito sonoro da coleta de frutas
            if(valor > 0):
                musica_coleta = pygame.mixer.Sound('music/coletar.wav')
            elif(valor < 0):
                musica_coleta = pygame.mixer.Sound('music/explodir.wav')
            musica_coleta.play()
        if self.pos_y >= 568:
            valor = 0
        return valor
