import datetime
d=int(input("digite o dia\n"))
m=int(input("digite o mes\n"))
a=int(input("digite o ano\n"))
x=datetime.datetime(a,m,d)
print(x.strftime("%d"),"de",x.strftime("%B"),"de",x.strftime("%Y"))