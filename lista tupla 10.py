mat=[]
for l in range (5):
    lin=[]
    for c in range (5):
        if l==c:
            lin.append(1)
        else:
            lin.append(0)
    mat.append(lin)
for i in mat:
    print (i)