from Produto import Produto
from Usuario import Usuario

while True:
    
    print("""
        1 - Cadastrar Produto
        2 - Cadastrar Usuario
        3 - Sair
        """)
    option=int(input())
    match option:
        case 1:
            marca=input("digite a marca do produto\n")
            expecificacao=input("digite a expecificação do produto\n")
            modelo=input("digite a modelo do produto\n")
            produto1=Produto(marca=marca,expecificacao=expecificacao,modelo=modelo)
            print(produto1.estoqueprodutos())
        case 2:
            nome=input("digite o nome do usuario\n")
            email=input("digite o email do usuario\n")
            senha=input("digite a senha do usuario\n")
            usuario1=Usuario(nome=nome,email=email,senha=senha)
            print(usuario1.arquivousuario())
        case 3:
            print("Obrigado")
            break
