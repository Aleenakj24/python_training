#reduce a no. to 1 and count the min no.of steps to do that
def fun(n):
    count=0
    if n==1:
        return 0
    elif n%2==0:
       
        return 1 + fun(n//2)
    else:
        return 1+min(fun(n-1),fun(n+1))

n=int(input())
print(fun(n)) 
   