n=[[1,2,3],
   [4,5,6],
   [7,8,9]]
g=[]
nt=[]
for i in n:
    g.append(i[0])
nt.append(g)
g=[]
for i in n:
    g.append(i[1])
nt.append(g)
g=[]
for i in n:
    g.append(i[2])
nt.append(g)
for i in nt:
    print(i)