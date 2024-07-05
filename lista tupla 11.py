f=[[1,2,11,13],
   [4,15,16,60],
   [7,8,19,200],
   [20,100,5,3]]
l=0
c=0
a=3
for i in f:
    for d in i:
        if d>a:
            a=d
            c=i.index(d)
            l=f.index(i)
print("linha",l+1,"coluna",c+1)