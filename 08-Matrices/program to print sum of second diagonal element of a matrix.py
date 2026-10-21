#program to print sum of second diagonal elements
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
    sum+=matrix[i][n-i-1]
print("sum of elements of second diagonal elements are: ",sum)

