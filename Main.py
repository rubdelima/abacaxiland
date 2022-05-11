import pygame
import random
from player import *
from ambiente import *
from objetos import *

pygame.init()
# Criando nosso player
player1 = Player(400, 500, 40, 4, False, False)

#Criando o Timer
clock = pygame.time.Clock()
counter, text = 60, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font3 = pygame.font.SysFont('Consolas', 18)

# Configurações da janela
screen = pygame.display.set_mode((900, 600)) #Criar a screen
background = pygame.image.load('images/background.png').convert_alpha() #Criar o background
pygame.display.set_caption("Abacaxiland") # Criando o nome da screen
icon = pygame.image.load('images/logo32.png').convert_alpha()
pygame.display.set_icon(icon)

# Musica de background
pygame.mixer.init()
pygame.mixer.music.load('music/background_music.wav')
pygame.mixer.music.play(-1)

# configurações de tempo do jogo
current_time = 0
interval = 0

# variáveis da pontuação das frutas
morango = Pontuacao_fruta('images/morango32.png', (255,0,0), 0, 20, 50)
abacaxi = Pontuacao_fruta('images/abacaxi32.png',(255,255,0), 0, 20, 88)
pitanga = Pontuacao_fruta('images/pitanga32.png',(255,100,100), 0, 20, 126)
banana = Pontuacao_fruta('images/banana32.png',(255,255,0), 0, 20, 164)

# bomb = Pontuacao_fruta('images/bomb.png', 0)
# nuclear = Pontuacao_fruta('images/nuclear-bomb.png', randint(0, 644))
# variável pra estabelecer o intervalo de tempo

aux = 0
spawn_origin = Spawn(0)

running = True
while running:
    aux += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = "Tempo restante: " + str(counter).rjust(3) 
    
    # screen do game
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
   
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


    spawn_origin.aparecer(screen, current_time, player1.pos_x, player1.pos_y)
    if spawn_origin.colisao() == True:
        
        # Efeito sonoro da coleta de frutas
        musica_coleta = pygame.mixer.Sound('music/coletar.wav')
        musica_coleta.play()
        
        fruta = spawn_origin.tipo
        if fruta == 0:
            morango.ponto += 1
        elif fruta == 1:
            abacaxi.ponto += 1
        elif fruta == 2:
            pitanga.ponto += 1
        elif fruta == 3:
            banana.ponto += 1

    pontuacao_total = Total(abacaxi.ponto + pitanga.ponto + morango.ponto + banana.ponto)
    pontuacao_total.mostrar_total(screen)
    # área da pontuação
    
    abacaxi.mostrar_pontos(screen)
    pitanga.mostrar_pontos(screen)
    morango.mostrar_pontos(screen)
    banana.mostrar_pontos(screen)
    
    #timer
    screen.blit(font3.render(text, True, (255, 255, 255)), (700,10 ))
    pygame.display.flip()
    clock.tick(60)
    

    
    pygame.display.update()
#funciona
pygame.quit()
