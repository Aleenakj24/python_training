# l=[1,2,3,4]
# x=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[len(l)-1]=x
# print(l)
# y=l[0]
# for i in range(len(l)-1):
#     l[i]=l[i+1]
# l[len(l)-1]=y
# print(l)

# rotate k times
l=[1,2,3,4]
temp=l[0]
for i in range(1,len(l)):
    l[i-1]=l[i]
l[-1]=temp
print(l)