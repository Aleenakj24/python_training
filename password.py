s=input()
alnum=0
lower=0
upper=0
special=0
if len(s)>=8:
    for i in s:
        if i.isalnum():
            alnum+=1
        elif i.islower():
            lower+=1
        elif i.isupper():
            upper+=1
        else:
            special+=1
if(len(s)>=8 and alnum>=1 and lower>=1 and upper>=1 and special>=1):
    print("valid")
else:
    print("invalid")


