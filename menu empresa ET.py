lu=[]
opcao=True
i=""
while opcao!=False:
    usuario=str(input("digite o nome de usuario\n"))
    senha=int(input("digite uma senha de 6 digitos\n"))
    
    if usuario=="administrador" and senha==123456:
        while i != "h":
            menuadministrador=str(input("digite a letra correspondente a opção desejada\na)cadastrar usuario\nb)listar usuario\nc)excluir usuario\nd)adcionar novo produto\ne)listar produto\nf)mostrar a quantidade de produtos\ng)excluir produto\nh)encerrar programa\n"))
            i == menuadministrador
            if menuadministrador=="a":
                usuario2=(str(input("digite o nome de usuario\n")))
                senha2=(int(input("digite uma senha de 6 digitos\n")))
                ap={'usuario':usuario2,'senha':senha2}
                lu.append(ap)

            elif menuadministrador=="b":
                c=0
                while c!=len(lu):
                    print(c,"-",lu[0+c])
                    c+=1
                
            #elif menuadministrador=="c":
                #excluirusuario=(str(input("digite o nome de usuario\n")))
                #lu.remove(excluirusuario)