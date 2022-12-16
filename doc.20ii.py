a=[20,37,20,21]
i=0
b=[]
while i<len(a):
    if a[i]not in b:
        b.append(a[i])
    i=i+1
print(b)    
