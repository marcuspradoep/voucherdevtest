th=int(input("digite o valor da hora\n"))
tm=int(input("digite o valor dos minutos\n"))
ts=int(input("digite o valor dos segundos\n"))
def sec(h,m,s):
    hs=h*3600
    hm=m*60
    tt=hs+hm+s
    return tt
print(sec(th,tm,ts))
