l=[[1,2,3],[4,5,6],[7,8,9]]
target=int(input())
row=len(matrix)
col=len(matrix[0])
s,e=0,(row*col)-1
while s<=e:
    m=(s+e)//2
    i=m//col
    j=m%col
    if matrix[i][j]==target:
        return True
    elif matrix[i][j]<target:
        s=m+1
    else:
        e=m-1
return False