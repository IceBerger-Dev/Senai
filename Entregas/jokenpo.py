jogador1 = str.lower(input('Jogador 1, escolha (pedra/papel/tesoura): '))

jogador2 = str.lower(input('Jogador 2 escolha (pedra/papel/tesoura): ')) 

combinacao = ['pedra > tesoura', 'tesoura > papel', 'papel > pedra']

if str(f'{jogador1} > {jogador2}') in combinacao:
    print(f'Jogador 1 ganhou, {jogador1} vence de {jogador2}')

elif jogador2 == jogador1:
    print('Empate')

elif str(f'{jogador2} > {jogador1}') in combinacao:
    print(f'Jogador 2 ganhou, {jogador2} vence de {jogador1}')
    
else:
    print('Algum dos jogadores não digitaram um valor correto! Tentem novamente')

