c=0
s=0
while True:
    n=float(input("digite uma nota de 0 a 10\n"))
    if n>=0 and n<=10:
        c+=1
        s+=n
    else:
        break
media=s/c
print(media)