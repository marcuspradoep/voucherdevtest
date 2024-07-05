contador=1

n1=int(input("digite um numero\n"))
n2=int(input("digite o expoente\n"))

if n2>0:
    for i in range(1,n2+1):
        contador*=n1
    print(contador)
else:
    print("1")