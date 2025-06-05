nome = str.capitalize(input('Digite seu nome: '))

listaNotas = []

contador = 0

while contador < 3:
    contador += 1
    nota = listaNotas.append(float(input(f'Digite sua nota {contador}: ')))

media =  sum(listaNotas)/len(listaNotas)

if media >= 7:
    print(f'{nome} você foi aprovado, sua média foi {media:.2f}')
elif 5 <= media < 7:
    print(f'{nome} você ficou de recuperação, sua média foi {media:.2f}')
else:
    print(f'{nome} você foi reprovado, sua média foi {media:.2f}')
