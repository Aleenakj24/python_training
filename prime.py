# n=int(input())
# flag=1
# if(n<=1):
#     flag=0
# for i in range(2,n//2+1):
#     if(n%i==0):
#         flag=0
# if(flag==0):
#     print("not")
# else:
#     print("prime")

n=int(input())
flag=1
if(n<=1):
    flag=0
for i in range(2,int(n**0.5)+1):
    if(n%i==0):
        flag=0
if(flag==0):
    print("not")
else:
    print("prime")
