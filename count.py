n=input().split()
l=[]
for i in n:
    if(n.count(i)%2!=0):
        l.append(n[i])
print(l)
        