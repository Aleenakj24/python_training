# # # n=int(input())
# # temp=n
# # rev=0
# # count=0
# # s=0
# # while(n!=0):
# #     rem=n%10
# #     count=count+1
# #     n=n//10

# # n=temp

# # while(n>0):
# #     rem=n%10
# #     s+=rem**count
# #     n=n//10
# # if(s==temp):
# #     print("arm")
# # else:
# #     print("not")



#pattern 21342- 2^0+4^1+3^2+2^3+1^4+2^5

# n=int(input())
# s=0
# count=1
# while(n!=0):
#     rem=n%10
#     s+=rem**count
#     n=n//10
#     count=count+1

# print(s)

#pattern 21342- 2^5+4^4+3^3+2^2+1^1+2^0

n=int(input())
s=0
count=0
temp=n
while(n!=0):
    rem=n%10
    count=count+1
    n=n//10
print(count)
n=temp
while(n>0):
    rem=n%10
    s+=rem**count
    n=n//10
    count=count-1
print(s)




