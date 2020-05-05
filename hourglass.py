mat = []
for i in range(6):
    mat.append([int(x) for x in input().split()])
i,j = 0,0
m = sum([mat[i][j],mat[i][j+1],mat[i][j+2],mat[i+1][j+1],mat[i+2][j],mat[i+2][j+1],mat[i+2][j+2]])

a = 6

abc = 0
for i in range(4):
    for j in range(4):
        abc=(mat[i][j]+mat[i][j+1]+mat[i][j+2])+ (mat[i+1][j+1])+ (mat[i+2][j]+mat[i+2]          [j +1]+mat[i+2][j+2]) 
        m = max(m,abc)
print(m)
