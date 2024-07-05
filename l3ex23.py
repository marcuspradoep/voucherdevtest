soma=0
n=int(input("digite um numero inteiro\n"))
for i in range(1,n):
    if n%i==0:
        soma+=i
        print(i)
print(soma)