#program to make second diagoanl elements zero
n=int(input("enter the size of a square matrix= "))
matrix=[]
print("enter elements= ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)
for i in range(n):
    matrix[i][n-i-1]=0
print("matrix is= ")
for row in matrix:
    print(row)

