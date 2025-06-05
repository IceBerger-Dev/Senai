valorCompra = float(input('Digite o valor da sua compra: '))

if valorCompra >= 100:
    print(f'Você teve um desconto de R${(valorCompra*0.1):.2f}.\nO valor final da sua compra é de R${valorCompra*0.9}')

else:
    print(f'Você não teve um desconto.\nO valor final da sua compra é de R${valorCompra}')