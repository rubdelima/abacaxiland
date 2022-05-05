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
        self.img = pygame.image.load(img)

    def coletar(self, janela):
        pass
    
        





class Spawn(Objetos):
    def __init__(self, aux=0):
        self.aux = aux
        
    def aparecer(self, janela, current_time, interval):
        
        self.aux += 1
        print(self.aux)
        if self.aux == 1:
            self.interval = 0
            self.tipo = randint(0, 3)
            if self.tipo == 0:
                self.fruta =  Objetos(64, 10, 0, 'images/morango.png', randint(0, 836))
            elif self.tipo == 1:
                self.fruta = Objetos(64, 5, 0, 'images/abacaxi.png', randint(0, 836))
            elif self.tipo == 2:
                self.fruta = Objetos(64, 7, 0, 'images/pitanga.png', randint(0, 836))
            elif self.tipo == 3:
                self.fruta = Objetos(64, 9, 0, 'images/banana.png', randint(0, 836))

        
        self.current_time = current_time
        self.interval = interval
        self.janela = janela

        # Aqui é onde a fruta é mostrada na tela
        if self.current_time - self.interval > 2000:
            self.fruta.pos_y += 1
            self.janela.blit(self.fruta.img, (self.fruta.pos_x, self.fruta.pos_y))
            if self.fruta.pos_y >= 568:
                self.aux = 0
        

    def aparecer_bomba(self):
        pass

    def aparecer_nuclear(self):
        pass
    

        





