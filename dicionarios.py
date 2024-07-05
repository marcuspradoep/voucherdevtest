lista=[]
for i in range(2):
    nome = input("DIGITE O NOME DA EMPRESA> ")
    unidade = input("DIGITE A UNIDADE> ")
    fone = input("DIGITE O TELEFONE> ")
    email = input("DIGITE O EMAIL> ")
    cidade = input("DIGITE A CIDADE> ")
    uf = input("DIGITE O ESTADO> ")
    pessoa = {'nome':nome, 'unidade':unidade,'fone':fone,'email':email,'cidade':cidade,'uf':uf}
    lista.append(pessoa)
      
    
print(lista)

