l=[6,2,1,3,4,5,6,7,8,9]
#123456789
l.sort()
r=[]
for i in l:
    if i%2!=0:
        r.append(i)
    else:
        r.insert(0,i)
print(r)