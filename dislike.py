#1560/A
t=int(input())
for i in range(t):#1,2,3,4,.......
    n=int(input())
    i=0
    k=1
    while 1:
        if i%3!=0 and i%10!=3:
            if n==k:
                print(i)
                break
            k=k+1#k should increment only when it is not divisble by 3 and not ending by 3
        i+=1
