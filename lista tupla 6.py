a=[("joao",8.0),("maria",9.5),("pedro",7.5),("ana",8.5)]
n=[]
t=''
p=7.0
for i in a:
    n.append(i[1])
    if i[1]>p:
        p=i[1]
        t=i[0]
print(t,p)