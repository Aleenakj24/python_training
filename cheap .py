#466A
n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*m)
else:
    print(((n//m)*b)+min(b,(n%m)*a))