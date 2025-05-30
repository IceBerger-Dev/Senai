#FAZER UMA CALCULADORA BASICA

inicio = ''

while inicio != 'n':

    inicio = str.lower(input("Deseja inciar uma operação? (s/n)"))
    if inicio == 'n':
        inicio = 's'
        break

    opcao = int(input("Qual das operações vc deseja realizar:" + "\n 1- Soma"+"\n 2- Subtração "+"\n 3- Multiplicação"+"\n 4- Divisão\n"))
    if opcao == 1:
        n1 = float(input("Digite o valor do primeiro número: "))
        n2 = float(input("Digite o valor do segundo número: "))
        soma = n1 + n2
        print(f"Valor da sua soma: {soma:.2f}")

    elif opcao == 2:
        n1 = float(input("Digite o valor do primeiro número: "))
        n2 = float(input("Digite o valor do segundo número: "))
        subtracao = n1 - n2
        print(f"Valor da sua subtração: {subtracao:.2f}")

    elif opcao == 3:
        n1 = float(input("Digite o valor do primeiro número: "))
        n2 = float(input("Digite o valor do segundo número: "))
        multiplicacao = n1 * n2
        print(f"Valor da sua multiplicação: {multiplicacao:.2f}")

    elif opcao ==4:
        n1 = float(input("Digite o valor do primeiro número: "))
        n2 = float(input("Digite o valor do segundo número: "))
        divisao = n1 / n2
        print(f"Valor da sua divisão: {divisao:.2f}")

    else:   
        print("Escolha uma opção desejada!") 
print("Volte sempre!")