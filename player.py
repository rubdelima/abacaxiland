import pygame

class Player():
    def __init__(self, pos_x, pos_y, tamanho, velocidade):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.tamanho = tamanho
        self.velocidade = velocidade

    def mover(self, comando): 

        # Mover o player com as setas (arrows keys):
        self.comando = comando
        if self.comando[pygame.K_UP] and self.pos_y >0:
            self.pos_y -= self.velocidade
        if self.comando[pygame.K_DOWN] and self.pos_y < 600:
            self.pos_y += self.velocidade
        if self.comando[pygame.K_LEFT] and self.pos_x > 0:
            self.pos_x -= self.velocidade
        if self.comando[pygame.K_RIGHT] and self.pos_x <900:
            self.pos_x += self.velocidade
    
    def desenhar_player(self, janela, playerimg):
        self.janela = janela
        self.playerimg = pygame.image.load(playerimg)
        self.janela.blit(self.playerimg, (self.pos_x, self.pos_y))

