soma=[]

n=int(input("digite um numero\n"))
if n>0:
    for i in range (n+1):
        soma.append(i)
    print(sum(soma))