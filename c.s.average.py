


a=[23,14,56,12,19,9,15,25,31,42,43]
i=0
s1=0
s2=0
c1=0
c2=0
while i<len(a):
    if (a[i])%2==0:
        s1=s1+(a[i])
        c1=c1+1
    else:
        s2=s2+(a[i])
        c2=c2+1
    i=i+1
print(" it is even number",s1)
print(" it is odd number",c1)
print(s2)
print(c2)


