import pygame
from random import randint
from player import *

class Objetos():

    def __init__(self, tamanho, valor, coletados, img, pos_x=randint(0,836), pos_y=0):
        self.tamanho = tamanho
        self.valor = valor
        self.coletados = coletados
        self.pos_x = pos_x 
        self.pos_y = pos_y 
        self.img = pygame.image.load(img).convert_alpha()

    def coletar(self, janela):
        pass

class Spawn(Objetos):
    def __init__(self, interval, aux=0):
        self.aux = aux
        self.interval = interval
        
    def aparecer(self, janela, current_time, player_x, player_y):
        self.player_x = player_x
        self.player_y = player_y
        self.aux += 1
        self.current_time = current_time
        
        if self.aux == 1:
            self.interval = 0
            self.tipo = randint(0, 3)
            if self.tipo == 0:
                self.fruta =  Objetos(64, 10, 0, 'images/morango64.png', randint(0, 836))
            elif self.tipo == 1:
                self.fruta = Objetos(64, 5, 0, 'images/abacaxi64.png', randint(0, 836))
            elif self.tipo == 2:
                self.fruta = Objetos(64, 7, 0, 'images/pitanga64.png', randint(0, 836))
            elif self.tipo == 3:
                self.fruta = Objetos(64, 9, 0, 'images/banana64.png', randint(0, 836))

        
        self.janela = janela

        # Aqui é onde a fruta é mostrada na tela
        if self.current_time - self.interval > 2000:
            self.fruta.pos_y += 1
            self.janela.blit(self.fruta.img, (self.fruta.pos_x, self.fruta.pos_y))
            if self.fruta.pos_y >= 568:
                self.aux = 0
            elif  self.player_y - 32 <= self.fruta.pos_y <= self.player_y + 32 and self.player_x - 32 <= self.fruta.pos_x <= self.player_x + 32:
                self.aux = 0    
                self.interval = current_time
                

    def colisao(self):
        colidiu = False
        if self.player_y - 32 <= self.fruta.pos_y <= self.player_y + 32 and self.player_x - 32 <= self.fruta.pos_x <= self.player_x + 32:
            colidiu = True
            self.aux = 0
        return colidiu
    def aparecer_bomba(self):
        pass

    def aparecer_nuclear(self):
        pass
    

        




