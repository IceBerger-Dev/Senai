#DESAFIO CALCULO DE PREVISÂO DE NORMAL
# - Para calcular a normal é preciso saber o apice dela, o número que se faz mais presente.
# - Depois achar os pontos de dispersão, onde existe menor frequencia antes do pico.
# - Calcular quartis e considerar apenas o segundo quartil para realizar o desvio

lista = []

inicio = int(input("Quantos números deseja digitar: "))

while inicio != 0:
    inicio -= 1
    num = lista.append(int(input("Digite um número:")))

lista.sort()

# moda = max(set(lista), key=lista.count)
# qtd_Moda = lista.count(moda)

media = sum(lista)//len(lista)
if media%2 != 0 and media%2 != 1:
    if round(media%2) == 0:
        media =+ 1


Q1 = ((len(lista))//4) + 1
Q2 = ((len(lista)*3)//4) + 1

if Q1 >= 3:

    del lista[(Q2-len(lista)):]
    del lista[:Q1-1]


lista_Calculo = []

for i in range(len(lista)):

    calculo =  lista_Calculo.append((media-lista[i])**2)

variancia = round(sum(lista_Calculo)/len(lista),2)
desvio = round((variancia ** 0.5),2)

if len(lista)%2 == 0:
    mediana = ( lista[(len(lista)//2)] + lista[((len(lista)//2)+1)] )/2
else:
    mediana = (lista[(len(lista)//2)])

print(f"O apice da sua normal é: {mediana}")

print(f"Seu desvio é: {desvio}")

print(f"A normal é {mediana}, considerando os desvios entre {mediana - desvio} e {mediana + desvio}")

print(f"A variancia é: {variancia}")

