#Dias da semana
dia = str.lower(input("Qual dia da semana vc tá? "))

match dia:
    case 'domingo':
        print('Você digitou um dia do final de semana!')
    case 'sábado':
        print('Você digitou um dia do final de semana!')
    case _ :
        print('Você digitou um dia útil!')
