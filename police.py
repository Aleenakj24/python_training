#427/A

p=0
u=0
l=list(map(int,input().split()))
for i in l:
    if i==-1:
        if p>0:
            p=p-1#crime done
        else:
            u=u+1
            
            
    else:
        p=p+i
print(u)
    












































































    