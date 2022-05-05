import pygame
import random
from player import *
from ambiente import *
from objetos import *

pygame.init()
# Criando nosso player
player1 = Player(400, 300, 40, 4)


# Configurações da janela
screen = pygame.display.set_mode((900, 600)) #Criar a screen
pygame.display.set_caption("Abacaxiland") # Criando o nome da screen
icon = pygame.image.load('images/logo.png')
pygame.display.set_icon(icon)

# configurações de tempo do jogo
current_time = 0
interval = 0
# variável pra estabelecer o intervalo de tempo
aux = 0

spawn_origin = Spawn()

running = True
while running:
    aux += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
    
    # screen do game
    screen.fill((133, 145, 42))
   
    # Movendo o personagem
    comando = pygame.key.get_pressed()
    player1.mover(comando)

    # desenho a posição do player na tela
    player1.desenhar_player(screen, 'images/player1.png')
    
    # ajeitando o tempo para o spawn
    current_time = pygame.time.get_ticks()
    if aux == 1:
        interval = current_time


    spawn_origin.aparecer(screen, current_time, interval)

    # área da pontuação
    pontos = Ambiente(0, 0)
    pontos.mostrar_total(screen)
    pontos.mostrar_pontos(screen, 'images/abacaxi.png', (255, 255, 0), abacaxi.coletados, 20, 40)
    pontos.mostrar_pontos(screen, 'images/pitanga.png', (255, 0, 0), pitanga.coletados, 20, 78)
    pontos.mostrar_pontos(screen, 'images/morango.png', (255,100, 0), morango.coletados, 20, 116 )
    pontos.mostrar_pontos(screen, 'images/banana.png', (255, 200, 0), banana.coletados, 20, 156)
    

    
    pygame.display.update()

pygame.quit()
