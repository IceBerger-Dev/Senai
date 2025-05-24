#PRIMEIRA ATIVIDADE
#-Calcular a media de 3 notas de um aluno, onde para passar a nota dele deve ser maior que <=7 para passar, >=5 ou >=7 recuperação, >5 reprova
nota1 = float(input("Digite o valor da sua primeira nota: "))
nota2 = float(input("Digite o valor da sua primeira segunda: "))
nota3 = float(input("Digite o valor da sua primeira tereceira: "))


media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"Você foi aprovado! Sua média foi: {media:.2f}" )
elif media < 5:
    print(f"Você foi reprovado! Sua média foi: {media:.2f}")
else:
    print(f"Você está de recuperação! Sua média foi: {media:.2f}")



#SEGUNDA ATIVIDADE