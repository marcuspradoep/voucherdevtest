idade=0
contador=0
while True:
    n=int(input("digite uma idade ou zero para terminar\n"))
    if n!=0:
        idade+=n
        contador+=1
        im=idade/contador
    elif n==0:
        break

print(im)