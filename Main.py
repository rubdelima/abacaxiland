import pygame
import random
from player import *
from ambiente import *
pygame.init()

caimento = 0
velocidade_caimento = 10

#coordenadas da bolona verde
# player1_x = 400
# player1_y = 300
# tam_bolona = 40
# velocity = 25
player1 = Player(400, 300, 40, 25)

#condição das bolinhas
bolinha_x = 400
bolinha_y = 100
tam_bolinha = 10
caimento = 0
velocidade_caimento = 10
#####################Score##############################################################
pontuacao_valor = 0
font = pygame.font.Font('freesansbold.ttf', 20)
textX = 10
textY = 10


abacaxi = azul = vermelho = verde = roxo = branco = 0


# Classe Ambiente sendo utilizada

    
time = 0

#########################################################################################

 #tipos de bolinha:
listas_de_bolinhas = ['abacaxi', 'azul', 'vermelho', 'verde', 'roxo', 'branco']
bolinhas = {"abacaxi" :"255,215,0", 'azul' :"0,255,255","vermelho" :"255,0,0", "verde" :"124,252,0","roxo" :"128,0,128", 'branco' :"255,255,255"}

def conversao_pont(a):
    global abacaxi
    global azul
    global vermelho
    global verde
    global roxo
    global branco
    if a == "abacaxi": abacaxi += 1
    if a == "azul": azul += 1
    if a == "vermelho": vermelho += 1
    if a == "verde": verde += 1
    if a == "roxo": roxo +=1
    if a == "branco": branco += 1

def nova_posicao():
    global bolinha_x
    global bolinha_y
    global velocidade_caimento
    random.seed();
    bolinha_x  = random.randint(100,700)
    bolinha_y  = 0
    velocidade_caimento +=3

def nova_cor():
    global gama1
    global gama2
    global gama3
    global bola_da_vez
    bola_da_vez = random.choice(listas_de_bolinhas)
    a = bolinhas[bola_da_vez]
    b,c,d = a.split(",")
    gama1 = int(b)
    gama2 = int(c)
    gama3 = int(d)
    
    
#########bola da vez#############
bola_da_vez = "verde"
gama1 = 0
gama2 = 255
gama3 = 0


janela = pygame.display.set_mode((900,600)) #Criar a janela
pygame.display.set_caption("Nosso Joguinho") # Criando o nome da janela

janela_aberta = True



while janela_aberta:
    pygame.time.delay(60) #colocar um delay pra as coisas não 'sumirem'
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #se apertat no botão de fechar alterar o valor do laço para falso
            janela_aberta = False
    
    time += 1
    # 
    comando = pygame.key.get_pressed()
    player1.mover(comando)
    
    #atualizar e não de bolinha_x r um "rastro"
    janela.fill((0,0,0))
    
    #nossa bolona
    player1.desenhar_player(janela, 'images/player1.png')
    #bolinhas para pegar
    pygame.draw.circle(janela, (gama1,gama2,gama3), (bolinha_x ,bolinha_y ), tam_bolinha) #o primeiro é o rgb (vermelho, verde, azul), o segundo é a posição e o último é o raio
    
    if (((bolinha_x - player1.pos_x)**2)+((bolinha_y - player1.pos_y)**2))**0.5 <= player1.tamanho:
        random.seed();
        bolinha_x  = random.randint(100,700)
        bolinha_y  = 0
        tam_bolinha = random.randint(10,40)
        velocidade_caimento +=1
        conversao_pont(bola_da_vez)
        nova_posicao()
        nova_cor()
        
    
    if bolinha_y > 600:
        bolinha_y = 0
        random.seed();
        bolinha_x  = random.randint(100,700)
        nova_cor()
    
    pontuacao_valor = (10*abacaxi) + (20*azul) + (-25*verde) + (vermelho*20) + (-30*branco) + (roxo*50)

    pontos = Ambiente(pontuacao_valor, 0)
    pontos.mostrar_total(janela)
    pontos.mostrar_pontos(janela, 'Abacaxi', (255, 255, 0), abacaxi, 40, 40)

    #movimentacao bolinha

    bolinha_y  += int(velocidade_caimento//10)
    
    pygame.display.update()

pygame.quit()
