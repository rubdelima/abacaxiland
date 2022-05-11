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
botao_restart_img = pygame.image.load('images/restart64.png').convert_alpha()

# Musica de background
pygame.mixer.init()
pygame.mixer.music.load('music/background_music.wav')
pygame.mixer.music.play(-1)

# configurações de tempo do jogo
current_time = 0
interval = 0

#Criando o Timer
clock = pygame.time.Clock()
counter, text = 61, '60'.rjust(3)
pygame.time.set_timer(pygame.USEREVENT, 1000)
font3 = pygame.font.SysFont('Consolas', 18)

# variáveis da pontuação das frutas
morango = Pontuacao_fruta('images/morango.png', (255,0,0), 0, 20, 50)
abacaxi = Pontuacao_fruta('images/abacaxi.png',(255,255,0), 0, 20, 88)
pitanga = Pontuacao_fruta('images/pitanga.png',(255,100,100), 0, 20, 126)
banana = Pontuacao_fruta('images/banana.png',(255,255,0), 0, 20, 164)


# Criando menu
menu = True
fonte_outlined = pygame.font.Font('fonte/vitamin_outlined.ttf', 80)
titulo_outlined = fonte_outlined.render(f'ABACAXILAND', True, (0,0,0))

fonte_regular = pygame.font.Font('fonte/vitamin_regular.ttf', 80)
titulo_regular = fonte_regular.render(f'ABACAXILAND', True, (255,255,0))


# Tela de fim de jogo
fonte_final_outlined = pygame.font.Font('fonte/vitamin_outlined.ttf', 80)
titulo_final_outlined = fonte_final_outlined.render(f'FIM DE JOGO', True, (0,0,0))

fonte_final_regular = pygame.font.Font('fonte/vitamin_regular.ttf', 80)
titulo_final_regular = fonte_final_regular.render(f'FIM DE JOGO', True, (255,255,0))

fonte_pontuacao_outlined = pygame.font.Font('fonte/vitamin_outlined.ttf', 40)
fonte_pontuacao_regular = pygame.font.Font('fonte/vitamin_regular.ttf', 40)

# Criar botões
botao_start = Botao(370, 300, botao_start_img)
botao_exit = Botao(370, 400, botao_exit_img) 
botao_restart = Botao(400, 350, botao_restart_img)

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
        if event.type == pygame.USEREVENT: 
            counter -= 1
            text = "Tempo restante: " + str(counter).rjust(3)
    
    # screen do game
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    
    if menu == True:
        # Nome do jogo
        screen.blit(titulo_outlined, (166, 150))
        screen.blit(titulo_regular, (165, 150))
        
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
            
        if counter > 0: # Mantém o jogo rodando enquanto o timer não chega a zero
            #pegando a diferença de objetos mostrado para serem adicionados de acordo com o nivel
            diff = abs(len(caindo) - nivel)
            if(diff != 0):
                objetos = [Objetos(64, 5, 'images/morango64.png', randint(0, 836)),Objetos(64, 10, 'images/abacaxi64.png', randint(0, 836)),Objetos(64, 9, 'images/pitanga64.png', randint(0, 836)),Objetos(64, 7, 'images/banana64.png', randint(0, 836)),Objetos(64, -10, 'images/bomb64.png', randint(0, 836))]
                for i in range(diff):
                    caindo.append(objetos[randint(0,4)])
            if(len(caindo) > 0):
                for obj in caindo:
                    obj.cair(screen,nivel)
                    valor = obj.colisao(player1.pos_x, player1.pos_y)
                    if(valor != -1):
                        if valor == 5:
                            morango.ponto += 1
                        elif valor == 10:
                            abacaxi.ponto += 1
                        elif valor == 9:
                            pitanga.ponto += 1
                        elif valor == 7:
                            banana.ponto += 1
                        if valor != 0:
                            total += obj.valor
                        if valor < 0:
                            counter -= 5
                        caindo.remove(obj)
            if(total < 0):
                total = 0
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
            screen.blit(font3.render(text, True, (255, 255, 255)), (700,10))
            pygame.display.flip()
            clock.tick(60)
        
        else:  # Quando o timer chega a zero, o jogo acaba
            # Texto de FIM DE JOGO e PONTUACAO
            screen.blit(titulo_final_outlined, (166, 150))
            screen.blit(titulo_final_regular, (165, 150))
            
            titulo_pontuacao_outlined = fonte_pontuacao_outlined.render(f'SUA PONTUACAO FOI: ' + str(total), True, (0, 0, 0))
            titulo_pontuacao_regular = fonte_pontuacao_regular.render(f'SUA PONTUACAO FOI: ' + str(total), True, (255, 255, 0))
            screen.blit(titulo_pontuacao_outlined, (191, 250))
            screen.blit(titulo_pontuacao_regular, (190, 250))
            
            # Botão para recomeçar o jogo
            if botao_restart.desenhar_botao(screen):
                counter = 61
                total = 0
                morango.ponto = 0
                abacaxi.ponto = 0
                banana.ponto = 0
                pitanga.ponto = 0
                nivel = 1
                caindo = []
                player1.pos_x = 400
                player1.pos_y = 500
                
                
                

    
    pygame.display.update()

pygame.quit()
