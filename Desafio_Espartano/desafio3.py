#CRIAR UM ALGORITMO QUE FAÇA O CALCÚLO DE MÉDIA, MODA, MEDIANA E QUARTIL
# -Média: Soma dos valores dividida pela quantidade deles
# -Moda: Número que mais aparece
# -Mediana: Número(s) central(is)
# -Quartil:
#     -Existem 3 quartis Q1, Q2 e Q3
#     --Primeiro quartil ou Q1:
#         Caso impar a quantidade de valores:
#             Q1 = (n+1)/4
#         Caso par:
#             Q1 = ((n/4) + ((n/4)+1))/2
#     --Segundo quartil ou Q2:
#         É a mediana
#     --Terceiro quartil ou Q3:
#         Q3 = Q2 + (Q2-Q1)
#         Caso seja par pode ser calculado de uma maneira diferente:
#             Q3 = ((3n/4)+((3n/4)+1))/2



valores = []

inicio = int(input("Quantos números deseja digitar: "))

while inicio != 0:
    inicio -= 1
    num = valores.append(int(input("Digite um número:")))


tam_Lista = len(valores)
valores.sort()

media = round((sum(valores)/tam_Lista),2)
moda = max(set(valores), key=valores.count)
qtd_Moda = valores.count(moda)
if (tam_Lista %2) == 0:
    #PAR

    #MEDIANA
    mediana1 = valores[((tam_Lista//2) -1)]
    mediana2 = valores[(tam_Lista//2)]
    mediana = (mediana1 + mediana2)/2

    #QUARTIL
    Q1 = (valores[(tam_Lista//4)] + valores[((tam_Lista//4)+1)])/2
    Q2 = mediana
    #             Q3 = ((3n/4)+((3n/4)+1))/2
    Q3= (valores[(3*tam_Lista//4)] + valores[((3*tam_Lista//4)+1)])/2

else:
    #IMPAR
    
    #MEDIANA
    mediana = valores[(tam_Lista//2)]

    #QUARTIL
    Q1= valores[((tam_Lista+1)//4)]
    Q2 = mediana
    Q3= Q2 + (Q2-Q1)

quartil = (f"O primeiro quartil é: {Q1}, o segundo quatil é: {Q2} e o terceiro quartil é: {Q3}")
    
print(f"Média: {media}",f"Moda:{moda} (aparece {qtd_Moda} vezes)",f"Mediana: {mediana}",f"Quartil: {quartil}", sep="\n")



# Duvidas
# -quartis na parte impar
# -questão da moda, precisei de auxilio, na parte do key, eu apenas declaro o objeto?
# -fiz as divisões gerarem numeros interos