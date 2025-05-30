# #DESAFIO DO ANO BISSEXTO
# - O ano é bissexto é divisivel por 4
# - O ano é bissexto se for divisivel por 400 em caso de centenario
# - O ano é bissexto se ele for divisivel por 400 em caso dele ser divisivel por 100

ano = int(input("Digite o ano que deseja descobrir se é bissexto: "))

if (ano%4) == 0 and (ano%100) !=0 and (ano%400) != 0:
    print("Esse ano é bissexto, ele é divisível por 4!")
elif (ano%400) !=0 and (ano%100) == 0:
    print("Esse ano não é bissexto, pois é divisivel por 100, porém não por 400")
elif (ano%400) == 0 and (ano%100) ==0:
    print("Esse ano é bissexto, pois é divisivel por 400!")
else:
    print("Esse ano não é bissexto!")