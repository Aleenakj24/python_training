# l=[1,2,3,4,5]
# for i in range(len(l)-1,-1,-1):
#     print(l[i])

l=list(map(int,input().split()))
j=len(l)-1#last elemt is stored
for i in range(len(l)//2):
    x=l[i]
    l[i]=l[j]
    l[j]=x
    j=j-1
print(l)




