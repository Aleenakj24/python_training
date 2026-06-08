s=input()
s1=[]
count=1
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        count+=1
    else:
        print(s[i],count,end="")
        count=1
print(s[i-1],count,end="")

s=input()
c,k=1,0
res=""
for i in range(1,len(s)):
    if(s[k]==s[i]):
        c+=1
    else:
        res+=s[i-1]+str(c)
        k=i
        c=1
res+=s[-1]+str(c)
print