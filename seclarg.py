# l=list(map(int,input().split()))
# m=max(l)
# l.remove(m)
# print(l)
# l.sort()
# print(l)
# print(max(l))
l=[5,4,3,2,1]
m1,m2=0,0
for i in l:
    if i>m1:
        m2=m1
        m1=i
    elif i>m2 and i!=m1:
        m2=i
print(m2)