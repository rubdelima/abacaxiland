import pygame

class Player():
    def __init__(self, pos_x, pos_y, tamanho, velocidade, pulo_up, pulo_down):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tamanho = tamanho
        self.velocidade = velocidade
        self.pulo_up = pulo_up
        self.pulo_down = pulo_down

    def mover(self, comando):
        # Mover o player com as setas (arrows keys):
        self.comando = comando
        if self.comando[pygame.K_UP] and self.pulo_up == False and self.pulo_down == False:
            self.pulo_up = True
        if self.comando[pygame.K_LEFT] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if self.comando[pygame.K_RIGHT] and self.pos_x <= 836:
            self.pos_x += self.velocidade
            
    def pular(self):
        
        if self.pulo_up:
            self.pos_y -= self.velocidade
        if self.pos_y <= 350:
            self.pulo_up = False
            self.pulo_down = True
            
        if self.pulo_down:
            self.pos_y += self.velocidade
        if self.pos_y >= 500:
            self.pulo_down = False
            
            
    def desenhar_player(self, janela, playerimg):
        self.janela = janela
        self.playerimg = pygame.image.load(playerimg).convert_alpha()
        self.janela.blit(self.playerimg, (self.pos_x, self.pos_y))
        

