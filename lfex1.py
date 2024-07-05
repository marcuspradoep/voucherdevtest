def fun():
    n=int(input("digite um numero\n"))
    p=int(input("digite um expoente\n"))

    cont=0
    while True:
        if cont<p:
            cont+=1
            r=n**cont
            print(n,"**",cont,"=",r)

fun()