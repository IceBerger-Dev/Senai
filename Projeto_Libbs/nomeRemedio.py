index = 5
comeca = 0
vogais = ['A', 'E', 'I', 'O', 'U']
nomePrincipio = str.upper(input('Digite o nome do principio ativo do seu medicamento: '))
listaPrincipio = list(nomePrincipio)
size = len(listaPrincipio)
print(listaPrincipio)
listaNomes = []
while index != 0:
    index -= 1
    indice = index
    for numero in size:
        if indice >= len(listaPrincipio):
            letra = listaPrincipio[comeca]
            letraAnterior = listaPrincipio[(numero-1)]
            listaPrincipio.append(letra)
            indice = comeca
            comeca += 1
        else:
            indice += 2
            letra = listaPrincipio[indice]
            letraAnterior = listaPrincipio[(numero-1)]
            if letra in vogais and letraAnterior in vogais:
                listaPrincipio.append(letra)

