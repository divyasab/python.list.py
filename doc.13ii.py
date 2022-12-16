# a=["aabcddddadnss"]
# i=0

a=["kama","tanu","divya"]
b=[["waghmare","21"],["khose","18"],["sable","20"]]
c=["surname","age"]
d={}
i=0
while i<len(a):
    d.update({a[i]:{c[0]:b[i][0],c[1]:b[i][1]}})
    i=i+1
print(d)
