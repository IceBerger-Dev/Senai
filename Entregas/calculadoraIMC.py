print('Bem-vindo a calculadora de IMC(Indice de Massa Corporal)')
peso = float(input('Digite o seu peso em quilogramas (kg): '))
altura = float(input('Digite sua altura em metros (m): '))

IMC = peso/(altura**2)

if IMC < 18.5:
    print(f'Seu IMC foi {IMC:.2f}. Você se enquadra no índice de Magreza')
elif 18.5 <= IMC < 24.9:
    print(f'Seu IMC foi {IMC:.2f}. Você se enquadra no índice de Normal')
elif 25 <= IMC < 29.9:
    print(f'Seu IMC foi {IMC:.2f}. Você se enquadra no índice de Sobrepeso')
elif 30 <= IMC < 39.9:
    print(f'Seu IMC foi {IMC:.2f}. Você se enquadra no índice de Obesidade')
else:
    print(f'Seu IMC foi {IMC:.2f}. Você se enquadra no índice de Obesidade Grave')
