
l=[1,3,1,2,1,4,2,2,2,2]
freq=[]
for i in l:
    n=l.count(i)
    freq.append(n)
print(max(freq))
for i in range(len(freq)):
    if freq[i]==max(freq):
        print(l[i])
        break
        #l[i] is printed because because freq have count, 
        #l have ellemnts both are having same index so weget the maxfreq,
        # using that i we can get corresponding elemnt from l



#using dict
# # l=[1,3,1,2,1,4,2,2,2,2]
# # d={}
# # for i in l:
# #     if i not in d:
# #         d[i]=1# if not in key, add key
# #     else:
# #         d[i]+=1#already pressent, increment key
# ele,max=0,0
# for i in d:
#     if d[i]>max:
#         max=d[i]
#         ele=i
    
# # print(ele)

