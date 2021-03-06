import pygame
from player import *
from ambiente import *
from objetos import *

pygame.init()
# Criando nosso player
player1 = Player(400, 500, 40, 10, False, False)


# Configurações da janela
screen = pygame.display.set_mode((900, 600)) #Criar a screen
background = pygame.image.load('images/background.png').convert_alpha() #Criar o blackground
pygame.display.set_caption("Abacaxiland") # Criando o nome da screen
icon = pygame.image.load('images/logo.png').convert_alpha()
pygame.display.set_icon(icon)

# Imagens dos botões
botao_start_img = pygame.image.load('images/start128_verde.png').convert_alpha()
botao_exit_img = pygame.image.load('images/exit128_verde.png').convert_alpha()

# Musica de background
pygame.mixer.init()
pygame.mixer.music.load('music/background_music.wav')
pygame.mixer.music.play(-1)

# configurações de tempo do jogo
current_time = 0
interval = 0

#Criando o Timer
clock = pygame.time.Clock()
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font3 = pygame.font.SysFont('Consolas', 30)

# Texto "Tempo"
texto = pygame.font.Font('freesansbold.ttf', 25)
texto_tempo = texto.render(f'Tempo:', True, (255, 255, 255))

# variáveis da pontuação das frutas
morango = Pontuacao_fruta('images/morango.png', (255,0,0), 0, 20, 50)
abacaxi = Pontuacao_fruta('images/abacaxi.png',(255,255,0), 0, 20, 88)
pitanga = Pontuacao_fruta('images/pitanga.png',(255,100,100), 0, 20, 126)
banana = Pontuacao_fruta('images/banana.png',(255,255,0), 0, 20, 164)


# Criando menu
menu = True
fonte = pygame.font.Font('fonte/Fresh Fruit.ttf', 70)
titulo = fonte.render(f'ABACAXILAND', True, (0, 204, 0))

# Criar botões
botao_start = Botao(370, 300, botao_start_img)
botao_exit = Botao(370, 400, botao_exit_img) 

aux = 0
caindo = []
nivel = 1
total = 0

running = True
while running:
    aux += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    # screen do game
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    if menu == True:
        # Nome do jogo
        screen.blit(titulo, (235, 150))
        
        if botao_exit.desenhar_botao(screen):
            running = False
        if botao_start.desenhar_botao(screen):
            menu = False
    else:
        # Movendo o personagem
        comando = pygame.key.get_pressed()
        player1.mover(comando)
        player1.pular()

        # desenho a posição do player na tela
        player1.desenhar_player(screen, 'images/player1.png')
        
        # ajeitando o tempo para o spawn
        current_time = pygame.time.get_ticks()
        if aux == 1:
            interval = current_time

        #pegando a diferença de objetos mostrado para serem adicionados de acordo com o nivel
        diff = abs(len(caindo) - nivel)
        if(diff != 0):
            objetos = [Objetos(64, 10, 'images/morango64.png', randint(0, 836)),Objetos(64, 5, 'images/abacaxi64.png', randint(0, 836)),Objetos(64, 7, 'images/pitanga64.png', randint(0, 836)),Objetos(64, 9, 'images/banana64.png', randint(0, 836)),Objetos(64, -10, 'images/bomb64.png', randint(0, 836))]
            for i in range(diff):
                caindo.append(objetos[randint(0,4)])
        if(len(caindo) > 0):
            for obj in caindo:
                obj.cair(screen,nivel)
                valor = obj.colisao(player1.pos_x, player1.pos_y)
                if(valor != -1):
                    if valor == 10:
                        morango.ponto += 1
                    elif valor == 5:
                        abacaxi.ponto += 1
                    elif valor == 7:
                        pitanga.ponto += 1
                    elif valor == 9:
                        banana.ponto += 1
                    if valor != 0:
                        total += obj.valor
                    caindo.remove(obj)

        if(total >= 50 and total < 100):
            nivel = 2
        elif(total >= 100):
            nivel = 3


        # área da pontuação
        pontuacao_total = Total(total)
        pontuacao_total.mostrar_total(screen)
        
        abacaxi.mostrar_pontos(screen)
        pitanga.mostrar_pontos(screen)
        morango.mostrar_pontos(screen)
        banana.mostrar_pontos(screen)
        
        #timer
        screen.blit(texto_tempo, (750, 10))
        screen.blit(font3.render(text, True, (255, 255, 255)), (840,10))
        pygame.display.flip()
        clock.tick(60)
    

    
    pygame.display.update()

pygame.quit()
