import pygame

class Ambiente():
    def __init__(self, pontuacao, vida):
        self.pontuacao = pontuacao
        self.vida = vida

    def mostrar_pontos(self, janela, nome, cor, pontuacao, pos_x, pos_y):
        self.janela = janela 
        self.nome = nome
        self.cor = cor
        self.pontuacao = pontuacao 
        self.pos_x = pos_x
        self.pos_y = pos_y

        fonte = pygame.font.Font('freesansbold.ttf', 20)
        aux = fonte.render(f'{nome}: '+ str(pontuacao), True, cor)
        janela.blit(aux, (pos_x, pos_y))

    def mostrar_vida():
        pass   

    def aplicar_pontos(self, nome):
        pass