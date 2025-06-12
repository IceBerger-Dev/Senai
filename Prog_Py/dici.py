# from teste import inserir


# dicionario  =  {}


# nome  = 'jose'


# lista = [25,'jose','rua 10']


# dados_usuaios = {
# 'nome':'Jose',
# 'idade':25,
# 'endereço':'rua 10',
# 'cursos':['js','python','java'],
# 'livros':{
# 'taleb':['cisne','antifragil'],
# 'arari':['futuro']  
# }
# }





# dicionario  = dict(a=10, b = 20, c = 10)
# print(dicionario)



lista_chaves = []
lista_valores = []


dic  =  {
'idade':[25,20,30],
'endereço':[],
'email':'@gmail'
}


dic['endereço'].append('Rua 20')
dic['endereço'].append('Rua 30')
print(dic)


for chave,valores in dic.items():
    lista_chaves.append(chave)
    lista_valores.append(valores)



print(lista_chaves, lista_valores)