#DESAFIO DA MÉDIA HARMÔNICA
# -Inverter os valores colocados
# -Somar todos os valores invetidos
# -Dividir pela quantidade de números
# -Inverter o resultado
# -O resultado da média artimetica dos inversos é o inverso da média harmônica.


qtd_Numeros = []
inicio = ''

while inicio != 'n':
    tam_Lista = len(qtd_Numeros)
    inicio = str.lower(input("Deseja informar?(s/n) "))

    if inicio != 'n':
        num = float(input("Digite um número:"))
        converte_Num =qtd_Numeros.append(round((1/num),2))

    else:
        #print("Caso tenha números digitados o suficiente iremos informar sua média harmônica!")

        if len(qtd_Numeros) <= 1:
            print("Você não tem itens o suficiente em sua lista para realizar a média harmônica")

        else:
            resultado = 1/((sum(qtd_Numeros))/tam_Lista)
            print(f"Aqui está sua média harmônica: {resultado:.2f} ")