import pygame

class Ambiente():
    def __init__(self, pontuacao, vida):
        self.pontuacao = pontuacao
        self.vida = vida


    def mostrar_total(self, janela):
        self.janela = janela
        fonte = pygame.font.Font('freesansbold.ttf', 20)
        aux = fonte.render(f'Pontuacao: '+ str(self.pontuacao), True, (255, 255, 255))
        janela.blit(aux, (10, 10))

    def mostrar_pontos(self, janela, img, cor, ponto, pos_x, pos_y):
        self.janela = janela 
        self.cor = cor
        self.ponto = ponto
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.img = pygame.image.load(img)
        fonte = pygame.font.Font('freesansbold.ttf', 20)
        aux = fonte.render(f'{str(ponto)}', True, cor)

        # display da pontuação na tela
        janela.blit(self.img, (pos_x, pos_y))
        janela.blit(aux, (pos_x+38, pos_y+10))  

    def mostrar_vida():
        pass   

    def aplicar_pontos(self, nome):
        pass

