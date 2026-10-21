#program to find difference of two matrix
rows=int(input("enter the number of rows= "))
cols=int(input("enter the number of columns= "))
print("enter the elements of first matrix= ")
a=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    a.append(row)
print("enter the elements of second matrix= ")
b=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(int(input()))
    b.append(row)

result=[]
for i in range(rows):
    row=[]
    for j in range(cols):
        row.append(a[i][j]-b[i][j])
    result.append(row)
print("resultant matrix= ")
for r in result:
    print(r)
