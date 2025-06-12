#Função e-mail

# email = str.lower(input('Digite se e-mail: '))

# def verifica(email):
#     if '@' in email and '.com' in email:
#         print('E-mail valido')
#     else:
#         print('Email inválido')

# verifica(email)

# Função Sistema de ponto

# entrada = str.lower(input('Digite o hoarário de entrada com dois pontos entre a hora e os minutos: '))
# saida = str.lower(input('Digite o hoarário de saída com dois pontos entre a hora e os minutos: '))

# listaEntrada = entrada.split(':')
# entrada = int(''.join(listaEntrada))

# listaSaida = saida.split(':')
# saida = int(''.join(listaSaida))

# def ponto(saida, entrada):
#     resultado = (saida - entrada)/100
    
#     if resultado < 8:
#         falta = str(round((8 - resultado),2))
#         listaFalta = falta.split('.')
#         falta = str(':'.join(listaFalta))

#         print(f'Você não bateu as horas trabalhadas, faltam {falta}')
#     else:
#         print('Você bateu as horas trabalhadas')

# ponto(saida, entrada)
#Função Geração de relatorios
vendas = []