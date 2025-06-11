#Com range

for numero in range(0, 200, 11):
    if numero%2 == 0:
        print(numero)
    else:
        numero += 1
        print(numero)

#Com lista

listaAnimais = ['gato', 'cachorro', 'pássaro', 'tigre']

for animal in listaAnimais:
    print(f'Animal: {animal}')


#Com Enumarate

listaNomes = ['Ana', 'Bruno', 'Carlos']

for x, nome in enumerate(listaNomes):
    print(f'{x}:{nome}')

for x, nome in enumerate(reversed(listaNomes)):
    print(f'{x}:{nome}')


#Com zip

listaProdutos = ['Arroz', 'Feijão', 'Café', 'Leite']
listaPrecos = [5.20, 04.50, 4.57, 5.30 ]

for produto, preco in zip(listaProdutos,listaPrecos):
    print(f'O {produto} tem o preço {preco: .2f}')


#Com String

palavra = 'Python é a melhor linguage do Mundo'

frase = [letra for letra in palavra]
print(frase)