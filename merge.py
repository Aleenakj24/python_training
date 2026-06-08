
# l1=[1,5,6]
# l2=[2,4,3]
# l3=l1+l2
# l3.sort()
# print(l3)
l1=[1,5,6]
l2=[2,3,4]
l3=[]
i,j=0,0
# for i in range(len(l1)-1):
#     for j in range(len(l2)-1):
while(i<len(l1) and j<len(l2)):
        if(l1[i]<l2[j]):
            l3.append(l1[i])
            i=i+1
        else:
            l3.append(l2[j])
            j=j+1


while(i<len(l1)):
       
        l3.append(l1[i])
        i=i+1

while(j<len(l2)):
       
        l3.append(l2[j])
        j=j+1

print(l3)