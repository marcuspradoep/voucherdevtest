soma=0
multi=1

n1=int(input("digite um numero\n"))
n2=int(input("digite outro numero\n"))
for i in range(n1,n2+1):
    if i%2==0:
        soma+=i
    elif i%2==1:
        multi*=i
soma+=(n1+n2)
multi*=(n1*n2)
print(soma)
print(multi)