a=[10,101,1000,10101]
i=0
b=[]
while i<len(a):
    d=str(a[i])
    j=0
    c=""
    while j<len(d):
        if d[j]!="0":
            c=c+d[j]
        j=j+1
    b.append(int(c))
    i=i+1
print(b)