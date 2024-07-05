
contador=0
pares=0
while True:
    n=int(input("digite um numero inteiro ou zero para terminar\n"))
    if n>0:
        contador+=1
        if n%2==0:    
            pares+=1
    elif n==0:
        break
print(contador)
print(pares)
