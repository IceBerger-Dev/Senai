# MANIPULAÇÃO DOS EVENTOS
# JOGO LABIRINTO

import pygame #realiza o import do game

# Inicializa o Pygame
pygame.init() #inicia a biblioteca



# COMENTE O CÓDIGO, EXPLIQUE COM SUAS PALAVRAS O QUE ESTA OCORRENDO EM CADA ESTRUTURA DO 
# CÓDIGO E VERIFIQUE O QUE OCORRE. 
# CONSULTE A BIBLIOTECA -> https://www.pygame.org/docs/





largura, altura = 400, 400 #defina o tamanho da exibição
tela = pygame.display.set_mode((largura, altura)) #define que a tela terá o tamanho definido na linha de cima
pygame.display.set_caption("Labirinto") #define o nome do game que será 'Labirinto'

#Tuplas de Cores que serão utilizadas no game
preto = (0, 0, 0) #cor dos obstáculos
branco = (255, 255, 255)#cor do caminho
vermelho = (255, 0, 0)#cor do "personagem"


tamanho_celula = 40 #preenchimento do labirinto na tela
labirinto = [ #aninhamento de listas
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
] #Basicamente uma estrutura similar a matriz que define onde será possivel passar com o personagem (0) e onde haverá obstaculos (1)


x, y = 3 * tamanho_celula, 3 * tamanho_celula #tamanho do personagem em relação ao preenchimento da tela
velocidade = 40 #velocidade que o personagem irá percorrer a cada ação nossa

def desenhar_labirinto(): #realiza um loop para pintar o labirinto de acordo com as definições da "matriz"
    for linha in range(len(labirinto)):#primeiro um looop para cada linha dessa matriz
        for coluna in range(len(labirinto[linha])):#aqui um loop para cada item dessa linha
            cor = preto if labirinto[linha][coluna] == 1 else branco#se 1 a cor deve ser preto, se não branco
            pygame.draw.rect(tela, cor, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))#realiza o desenha retangular levando em consideração a
            #determinação dos tamanhos e alturas antes colocados


executando = True 
while executando: #enquanto a variavel 'executando' for verdadeira o jogo seguirá
    for evento in pygame.event.get(): #para cada evento dentro do nosso jogo, #caso o jogador desejar sair
        if evento.type == pygame.QUIT:#caso o jogador desejar sair
            executando = False#defina 'executando' como falso


    teclas = pygame.key.get_pressed() #cria uma vaiavel para armazenar as ações das teclas do teclado
    if teclas[pygame.K_LEFT]:
        novo_x = x - velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0: #define qual tecla será responsavel por uma ação e realiza uma divisão ideal que caso de 0
            x = novo_x  #ou seja, o caminho seja branco o personagem se mexe
    if teclas[pygame.K_RIGHT]:
        novo_x = x + velocidade
        if labirinto[y // tamanho_celula][novo_x // tamanho_celula] == 0:
            x = novo_x
    if teclas[pygame.K_UP]:
        novo_y = y - velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y
    if teclas[pygame.K_DOWN]:
        novo_y = y + velocidade
        if labirinto[novo_y // tamanho_celula][x // tamanho_celula] == 0:
            y = novo_y


    tela.fill(branco) #define o preenchimento do nosso game como branco

    
    desenhar_labirinto() #realiza as ações de maneira grafica depois das condições
    pygame.draw.rect(tela, vermelho, (x, y, tamanho_celula, tamanho_celula)) #faz nosso personagem se mover


    pygame.display.flip()#atualização da tela inteira pra mostrar o andamento do game


    pygame.time.Clock().tick(10)#define o tempo de resposta para o personagem andar (taxa de quadros, quanto maior mais rapido em relação ao click)


pygame.quit() #fecha nosso game