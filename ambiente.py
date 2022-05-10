import pygame

class Total():
    def __init__(self, pontuacao=0):
        self.pontuacao = pontuacao
        


    def mostrar_total(self, janela):
        self.janela = janela
        fonte = pygame.font.Font('freesansbold.ttf', 20)
        aux = fonte.render(f'Pontuacao: '+ str(self.pontuacao), True, (255, 255, 255))
        janela.blit(aux, (10, 10))

    
class Vida():
    def mostrar_vida(sef):
        pass   


class Pontuacao_fruta():
        def __init__(self, img, cor, ponto, pos_x=0, pos_y=0):
            
            self.cor = cor
            self.ponto = ponto
            self.pos_x = pos_x
            self.pos_y = pos_y
            self.img = pygame.image.load(img)



        def mostrar_pontos(self, janela):
            self.janela = janela
            self.fonte = pygame.font.Font('freesansbold.ttf', 20)
            aux = self.fonte.render(f'{str(self.ponto)}', True, self.cor)

            # Mostra a pontuacao das frutas individualmente
            self.janela.blit(self.img, (self.pos_x, self.pos_y))
            self.janela.blit(aux, (self.pos_x+38, self.pos_y+10))

        def coletar(self):  
            pass
        
# Criando os botões do menu
class Botao:
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.clique = False
        
    def desenhar_botao(self, janela):
        self.janela = janela
        acao = False
        
        # Pegar posição do mouse
        pos = pygame.mouse.get_pos()
        
        # Checar ações do mouse
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clique == False:
                acao = True
                self.clique = True
                # Efeito sonoro de clicar no botão de start
                musica_coleta = pygame.mixer.Sound('music/menu_clique.wav')
                musica_coleta.play()
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clique = False
            
        # Desenhar botão
        self.janela.blit(self.image, self.rect)
        
        return acao