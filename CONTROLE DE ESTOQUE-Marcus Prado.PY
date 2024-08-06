administlistadeusuario=[]
listadesenha=[]
listadeprodutos=[]
i = ""
opcao=True
while opcao!=False:
    usuario=str(input("digite o nome de usuario\n"))
    senha=int(input("digite uma senha de 6 digitos\n"))
    if usuario=="administrador" and senha==123456:
        while i != "h":
            menuadministrador=str(input("digite a letra correspondente a opção desejada\na)cadastrar usuario\nb)listar usuario\nc)excluir usuario\nd)adcionar novo produto\ne)listar produto\nf)mostrar a quantidade de produtos\ng)excluir produto\nh)encerrar programa\n"))
            i == menuadministrador
            if menuadministrador=="a":
                listadeusuario.append(str(input("digite o nome de usuario\n")))
                listadesenha.append(int(input("digite uma senha de 6 digitos\n")))


            elif menuadministrador=="b":
                c=0
                while c!=len(listadeusuario):
                    print(c,"-",listadeusuario[0+c])
                    c+=1


            elif menuadministrador=="c":
                excluirusuario=(str(input("digite o nome de usuario\n")))
                listadeusuario.remove(excluirusuario)


            elif menuadministrador=="d":
                listadeprodutos.append(str(input("digite o produto-expecificação\n")))


            elif menuadministrador=="e":
                p=0
                while p!=len(listadeprodutos):
                    print(p,"-",listadeprodutos[0+p])
                    p+=1


            elif menuadministrador=="f":
                verificarquantidade=(str(input("digite o produto-expecificação\n")))
                q = -1
                contador=0
                print("a quantidade total de produtos são",len(listadeprodutos))
                while q<len(listadeprodutos)-1:
                    q+=1
                    if listadeprodutos[q] !=verificarquantidade:
                        continue
                    else:
                        contador += 1
                print("a quantidade de",verificarquantidade,"encontrada é",contador)


            elif menuadministrador=="g":
                excluirproduto=(str(input("digite o produto-expecificação\n")))
                listadeprodutos.remove(excluirproduto) 
                if len(listadeprodutos)== 0:
                     print("comprar mais",excluirproduto,"\n", listadeprodutos)


            else:
                break


    opcao=True
    while opcao!=False:
        usuario=str(input("digite o nome de usuario\n"))
        senha=int(input("digite uma senha de 6 digitos\n"))
        if usuario=="jose" and senha==654321:
                while i != "d":
                    menufuncionario=str(input("digite a letra correspondente a opção desejada\na)adcionar novo produto\nb)listar produto\nc)mostrar a quantidade de produtos\nd)excluir produto\ne)encerrar programa\n"))
                    i == menufuncionario
                    if menufuncionario=="a":
                        listadeprodutos.append(str(input("digite o produto-expecificação\n")))
                    elif menufuncionario=="b":
                        p=0
                        while p!=len(listadeprodutos):
                            print(p,"-",listadeprodutos[0+p])
                            p+=1


                    elif menufuncionario=="c":
                        verificarquantidade=(str(input("digite o produto-expecificação\n")))
                        q = -1
                        contador=0
                        print("a quantidade total de produtos são",len(listadeprodutos))
                        while q<len(listadeprodutos)-1:
                            q+=1
                            if listadeprodutos[q] !=verificarquantidade:
                                continue
                            else:
                                contador += 1
                        print("a quantidade de",verificarquantidade,"encontrada é",contador)


                    elif menufuncionario=="d":
                        excluirproduto=(str(input("digite o produto-expecificação\n")))
                        listadeprodutos.remove(excluirproduto) 
                        if len(listadeprodutos)== 0:
                            print("comprar mais",excluirproduto,"\n", listadeprodutos)

                            
                    else:
                        break
                
        
        
    