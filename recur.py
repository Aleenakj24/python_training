# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
# n=5
# fun(5)


# #12345
# def fun(n):
#     if n==0:
#          return
#     fun(n-1)
#     print(n)
     
# n=5
# fun(5)


# def fun(n):
#     if(n==0):
#         return
#     print(n)
#     fun(n-2)
# n=10
# fun(10)

#246810

# def fun(n):
#     if n==0:
#          return
#     fun(n-2)
#     print(n)

# fun(10)

# def fun(n):
#     if n==6:
#         return
#     print(n)
#     fun(n+1)
# fun(1)

# def fun(n):
#     if(n==10):
#         return
#     print(n)
#     fun(n+2)
# fun(2)

# def fun(n):
#     if n==0:
#         return
#     print(n)
#     fun(n-1)
#     print(n)
# fun(5)

# def fun(n):
#     if n==0:
#         return
#     fun(n-1)
#     print(n)
#     fun(n-1)
# fun(5)

# def fun(n):
#     if n==0:
#         return 200
    
#     x=fun(n-1)
#     print(n)
#     return x

# x=fun(5)
# print(x)


#123454321
def fun(n):
    if n==0:
        return
    print(n)
    fun(n-1)
   
    if n!=1:
        print(n)
fun(5)

#123454321

def fun(n,m=0):
    if n==m:
        return m
    print(m+1,end=" ")
    fun(n,m+1)
    print(m+1)