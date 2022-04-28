import pygame
import random
pygame.init()

#coordenadas da bolona
x = 400
y = 300
tam_bolona = 40

velocity = 25
#condição da bolinha
bolinhas = True
xa= 100
ya= 100
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
        y -= velocity
    if comandos[pygame.K_DOWN]:
        y += velocity
    if comandos[pygame.K_LEFT]:
        x -= velocity
    if comandos[pygame.K_RIGHT]:
        x += velocity
    
    #atualizar e não deixar um "rastro"
    janela.fill((0,0,0))
    
    #nossa bolona
    pygame.draw.circle(janela, (0,255,0), (x,y), tam_bolona) #o primeiro é o rgb (vermelho, verde, azul), o segundo é a posição e o último é o raio
    #bolinhas para pegar
    pygame.draw.circle(janela, (255,0,0), (xa,ya), tam_bolinha) #o primeiro é o rgb (vermelho, verde, azul), o segundo é a posição e o último é o raio
    
    if (xa+tam_bolinha - x+tam_bolona == 0) or (ya+tam_bolinha - y+tam_bolona == 0):
        tam_bolona += tam_bolinha
        random.seed();
        xa = random.randint(100,700)
        ya = random.randint(100,500)
        tam_bolinha = random.randint(10,40)
        
    
    pygame.display.update()

pygame.quit()