num=[]
n=int(input("digite a quantidade de numeros desejada\n"))
while len(num)<n:
    s=int(input("digite um numero\n"))
    num.append(s)
print(max(num))