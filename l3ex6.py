soma=0
for s in range(10):
    n=float(input("digite um numero\n"))
    soma+=n
print(soma)
print("\n")

contador=0
soma2=0
while(contador<10):
    s2=float(input("digite um numero\n"))
    soma2+=s2
    contador+=1
    if contador==10:
        break
print(soma2)