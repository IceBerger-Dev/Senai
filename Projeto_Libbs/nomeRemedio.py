import random
nomePrincipio = str.upper(input('Digite o nome do principio ativo do seu medicamento: '))
listaPrincipio = list(nomePrincipio)
print(listaPrincipio)

nomeRemedio = random.sample(listaPrincipio, k=5)
print(nomeRemedio)
