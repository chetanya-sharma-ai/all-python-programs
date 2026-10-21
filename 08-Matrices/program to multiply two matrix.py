#program to multiply two matrix using nested loop

X=[[1,2,3],[2,1,2],[1,3,2]]
Y=[[1,2,3],[3,1,2],[2,1,3]]

result=[[0,0,0]],[[0,0,0]],[[0,0,0]]
for i in range(len(X)):

    for j in range(len(Y[0])):
        for k in range(len(Y)):
            result[i][j]=result[i][j]+X[i][j]*Y[k][j]

for r in result:
    print(r)
