# l=[2,3,1,5,2,4,6,7,8,5,2,2,3]
# k=int(input())
# m=0
# for i in range(len(l)-k):
#     s=0
#     for j in range(i,i+k):
#         s+=l[j]
#     m=max(m,s)
# print(m)

l=[2,3,1,5,2,4,6,7,8,5,2,2,3]
k=int(input())
s=sum(l[:k])
m=s
for i in range(len(l)-k+1):
    s=0
    for j in range(i,i+k):
        s+=l[j]
    m=max(m,s)
print(m)