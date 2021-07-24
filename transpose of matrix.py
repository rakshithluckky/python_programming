A=[[1,2],[4,5],[7,8]]
result=[[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        result[j][i]=A[i][j]
for r in result:
    print(r)
