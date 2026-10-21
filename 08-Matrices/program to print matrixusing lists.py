#programto print diaginal elements of a given matrix
n=int(input("enter the size of a square matrix"))
matrix=[]
print("enter elements")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)
print("diagonal elements are:")
for i in range(n):
    print(matrix[i][i], end=" ")
