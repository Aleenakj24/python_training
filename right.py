l=[1,2,3,4]
x=l[len(l)-1]
for i in range(len(l)-1,-1,-1):
    l[i]=l[i-1]
l[0]=x
print(l)