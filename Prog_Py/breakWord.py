fraseCompleta = 'A inteligência artificial está revolucionando o mundo, transformando a maneira como interagimos com a tecnologia e impulsionando o progresso em diversas áreas.'

listaPalavras = fraseCompleta.split(sep=' ')

frase1= []
frase2= []

complete = 0

for palavra in listaPalavras:
    print(palavra)
    resultado = ' '.join(frase1)
    if (len(resultado) + len(palavra) + complete) < 72:
        frase1.append(palavra)
    else:
        complete = (len(resultado) + len(palavra) + complete) - 72
        frase2.append(palavra)

print(' '.join(frase1))
print(' '.join(frase2))