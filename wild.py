# def wild(grid,i,j):
#     if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]!=1:
#         return
#     grid[i][j]=-1
#     wild(grid,i+1,j)
#     wild(grid,i-1,j)
#     wild(grid,i,j+1)
#     wild(grid,i,j-1)

# matrix=[[1,1,1,1],
# [1,0,0,0],
# [0,0,1,1],
# [1,0,0,0]]
# wild(matrix,0,0)
# c=0
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         if matrix[i][j]==1:
#             c+=1
# print(c)

#island path
def maze(grid,path,i,j,n):
    if i==n and j==n:
        print(path)
        return
    if i+1<=n and grid[i+1][j]==1:
        maze(grid,path+'D',i+1,j,n)
    if j+1<=n and grid[i][j+1]==1:
        maze(grid,path+'R',i,j+1,n)

grid=[[1,1,1,1],
[1,0,0,0],
[0,0,1,1],
[1,0,0,0]]
n=len(grid)
maze(grid,"",0,0,n-1)