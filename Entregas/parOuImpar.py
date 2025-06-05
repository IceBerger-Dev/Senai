escolha = str.lower(input('Jogador 1 escolha par ou impar? '))

jogador1 = int(input('Digite um número, Jogador 1: '))
jogador2 = int(input('Digite um número, Jogador 2: '))

soma = jogador1 + jogador2

if soma % 2 == 0:
    resultado = 'par'
else:
    resultado = 'impar'

if escolha == resultado:
    print(f'O jogador 1 ganhou, pois deu {resultado}')
else:
    print(f'O jogador 2 ganhou, pois deu {resultado}')