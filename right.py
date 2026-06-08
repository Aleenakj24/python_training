# l=[1,2,3,4]
# x=l[len(l)-1]
# for i in range(len(l)-1,-1,-1):
#     l[i]=l[i-1]
# l[0]=x
# print(l)


# # rotate 2 times
# l=[1,2,3,4]
# x=l[-2]
# y=l[-1]
# for i in range(len(l)-1,-1,-1):
#     l[i]=l[i-2]

# l[0]=x
# l[1]=y
# print(l)

# #rotate k times-brute force
# l=[1,2,3,4,5,6,7]
# k=int(input())
# k=k%len(l)
# for i in range(k):
#     x=l[len(l)]
#     for i in range(len(l)-1,-1,-1):
#         l[i]=l[i-1]
#     l[0]=x
# print(l)

# l=[1,2,3,4,5,6,7]
# k=int(input())
# length=k%len(l)
# l1=l[0:length]
# l1.reverse()
# l2=l[length:len(l)]
# l2.reverse()
# l3=l1+l2
# l3.reverse()
# print(l3)


# #left rotation
# l=[1,2,3,4,5,6,7]
# k=int(input())
# k=k%len(l)
# def rotate(i,j):
#     while(i<j):
#         l[i],l[j]=l[j],l[i]
#         i=i+1
#         j=j-1


# rotate(0,k)
# rotate(k+1,len(l)-1)
# rotate(0,len(l)-1)
# print(l)

#right rotation
l=[1,2,3,4,5,6,7]
k=int(input())
k=k%len(l)
def rotate(i,j):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1

rotate(0,len(l)-1)
rotate(0,k-1)
rotate(k,len(l)-1)

print(l)