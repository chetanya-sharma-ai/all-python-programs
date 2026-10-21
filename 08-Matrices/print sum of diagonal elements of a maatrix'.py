#program to print sum of diagonal elements of a matrix
n=int(input("enter the size of a square matrix= "))
matrix=[]
print("enter elements= ")
for i in range(n):
    row=[]
    for j in range(n):
        row.append(int(input()))
    matrix.append(row)
sum=0    
for i in range(n):
    sum+=matrix[i][i]
print("sum of diagonal elements of matrix= ",sum)    
