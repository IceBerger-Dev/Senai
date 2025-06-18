import random


def ex4():
    for i in range(10, 0, -1):
        print(i)
    print('Fogo')



def ex5():
    num = int(input('Digite um número inteiro e positivo: '))
    pares = []

    for i in range(2, num, 2):
        pares.append(i)

    print(f'A soma de todos números pares até o número que vc digitou é: {sum(pares)}')



def ex6():
    num = int(input('Digite um número para saber a tabuada dele: '))
    print('A tabuada desse número é: ')
    for i in range(1, 11):
        print(f'{num} x {i}: {(num*i)}')



def ex7():
    for i in range(99, 0, -2):
        print(i)