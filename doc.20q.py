# Write a function that takes one argument “n” and delete that many elements from
#  the list.

# delete_nth ([1,1,1,1],2) # return [1,1]
a=[1,1,1,1]
i=0
b=[]
while i<len(a):
    if a[i] not in b:
        b.append(a[i])
    i=i+1
print(b)
