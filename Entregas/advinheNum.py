import random

numeroMisterioso = random.randint(1,5)

tentativas = 3
acerto = False

while tentativas != 0:
    tentativas -= 1
    numero = int(input('Digite um número para tentar advinhar o número misterioso: '))

    if numero == numeroMisterioso:

        print(f'Você ganhou, o número é {numero}')
        tentativas = 0
        acerto = True

    else:

        print(f'Não foi dessa, o número misterioso não é {numero}.\nTente de novo, restam {tentativas} tentativas\n')

if acerto == False:
    print(f'O número misterioso era {numeroMisterioso}')

