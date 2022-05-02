import pygame
import random
pygame.init()

caimento = 0

#coordenadas da bolona verde
player_x = 400
player_y = 300
tam_bolona = 40
velocity = 25
#condição da bolinha vermelha
bolinha_x = 100
bolinha_y = 100
tam_bolinha = 10

janela = pygame.display.set_mode((800,600)) #Criar a janela
pygame.display.set_caption("Nosso Joguinho") # Criando o nome da janela

janela_aberta = True

while janela_aberta:
    pygame.time.delay(60) #colocar um delay pra as coisas não 'sumirem'
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #se apertat no botão de fechar alterar o valor do laço para falso
            janela_aberta = False
        
    #comandos para movimentar a bolona
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        player_y -= velocity
    if comandos[pygame.K_DOWN]:
        player_y += velocity
    if comandos[pygame.K_LEFT]:
        player_x -= velocity
    if comandos[pygame.K_RIGHT]:
        player_x += velocity
    # if comandos[pygame.K_SPACE]:
    #     tam_bolona += 5
    
    #atualizar e não deibolinha_x r um "rastro"
    janela.fill((0,0,0))
    
    #nossa bolona
    pygame.draw.circle(janela, (0,255,0), (player_x, player_y), tam_bolona) #o primeiro é o rgb (vermelho, verde, azul), o segundo é a posição e o último é o raio
    #bolinhas para pegar
    pygame.draw.circle(janela, (255,0,0), (bolinha_x ,bolinha_y ), tam_bolinha) #o primeiro é o rgb (vermelho, verde, azul), o segundo é a posição e o último é o raio
    
    if ((bolinha_x + tam_bolinha) - (player_x + tam_bolona)) >= 0 and ((bolinha_y + tam_bolinha) - (player_y + tam_bolona) >= 0):
        random.seed();
        tam_bolona += 10
        bolinha_x  = random.randint(100,700)
        bolinha_y  = 0
        tam_bolinha = random.randint(10,40)

    
    #movimentacao bolinha
    caimento += 1
    if caimento == 10:
        bolinha_y  += 10
        caimento = 0
    
        
    
    pygame.display.update()

pygame.quit()
