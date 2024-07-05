f=[[1,2,11,13],
   [4,15,16,60],
   [7,8,19,200],
   [20,100,5,3]]
m=[]
for i in f:
    for e in i:
        if e>10:
            m.append(e)
print(len(m))
