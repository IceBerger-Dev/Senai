# # e-commerce

# # cadastrar

# dados = {}
# print('CAdastre-se: ')
# email = input('E-mail: ')
# senha = input('senha: ')

# dados['e-mail'] = email
# dados['senha'] = senha

# # acesso ao sistema

# print('-----||------||-------||-------')
# print('Seja bem vindo(a) ao e-commerce ZZZ')
# print('Acesse a aplicação')

# chances = 3

# carrinho = []
# meu_total = []
# lista_prod = ['','pipoca','arroz','milho','quentão']
# valor_prod = ['',2.0,10.0,20.0,15.50]

# while chances > 0:
#     email_acesso = input('Digite seu e-mail')
#     senha_acesso = input('Digite sua senha')

#     if email_acesso == dados['e-mail'] and senha_acesso == dados['senha']:
#         print('Sejam bem vindo a sua conta ')
#         acesso  = input('Deseja pedir? s/n')
#         print(lista_prod)
#         # escolher produto
#         while acesso == 's':
#             pedido = int(input('Digite o ID do produto 1 -2 -3 -4')) 
#             carrinho.append(lista_prod[pedido])
#             meu_total .append(valor_prod[pedido])
#             print(carrinho)
#             soma =  sum(meu_total)
#             print('R$',soma)
#             acesso  = input('Deseja pedir? s/n')
#         else:
#             print('Obrigado volte sempre')
#             print('Total  -  R$',soma)
                    
#             lista_pag = ('','PIX','CC','CD')
#             print(lista_pag)
#             forma_pag = int(input('Digite o ID forma de pagamento'))
#             print(lista_pag[forma_pag])
#         break    
#     else:
#         print('Erro de digitação')
#         chances = chances -1    
# else:
#     print('Bloqueio de conta ')
# 
#  
'---------------------------------------------------------'
import auto_py_to_exe as auto


# e-commerce

# cadastrar
def e_commerce():
    dados = {}
    print('CAdastre-se: ')
    email = input('E-mail: ')
    senha = input('senha: ')

    dados['e-mail'] = email
    dados['senha'] = senha

    # acesso ao sistema

    print('---' * 20)
    print('Seja bem vindo(a) ao e-commerce ZZZ')
    print('Acesse a aplicação')

    chances = 3

    carrinho = []
    meu_total = []
    lista_prod = ['','pipoca','arroz','milho','quentão']
    valor_prod = ['',2.0,10.0,20.0,15.50]
    while chances > 0:
        email_acesso = input('Digite seu e-mail')
        senha_acesso = input('Digite sua senha')

        if email_acesso == dados['e-mail'] and senha_acesso == dados['senha']:
            print('Sejam bem vindo a sua conta ')
            acesso  = input('Deseja pedir? s/n')
            print(lista_prod)
            # escolher produto
            while acesso == 's':
                pedido = int(input('Digite o ID do produto 1 -2 -3 -4')) 
                carrinho.append(lista_prod[pedido])
                meu_total .append(valor_prod[pedido])
                print(carrinho)
                soma =  sum(meu_total)
                print('R$',soma)
                acesso  = input('Deseja pedir? s/n')
            else:
                print('Obrigado volte sempre')
                print('Total  -  R$',soma)
                        
                lista_pag = ('','PIX','CC','CD')
                print(lista_pag)
                forma_pag = int(input('Digite o ID forma de pagamento'))
                print(lista_pag[forma_pag])
            break    
        else:
            print('Erro de digitação')
            chances = chances -1    
    else:
        print('Bloqueio de conta ')


while True:
    e_commerce()
    v = input('Digite enter para sair')
