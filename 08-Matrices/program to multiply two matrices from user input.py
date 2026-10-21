#program to multiply two matrices:
r1=int(input("enter the rows of first matrix: "))
c1=int(input("enter the columns of first matrix: "))

r2=int(input("enter the rows of second matrix: "))
c2=int(input("enter the columns of second matrix: "))

if c1!=r2:
    print("matrix multiplacation is not possible.")
else:
    print("enter the elements of first matrix: ")
    a = []
    for i in range (r1):
        row = []
        for j in range(c1):
            row.append(int(input()))
        a.append(row)

    print("enter the elements of second matrix: ")
    b = []
    for i in range(r2):
        row = []
        for j in range(c2):
            row.append(int(input()))
        b.append(row)
#initialize result matrix with zeroes
    result = []
    for i in range(r1):
        row = []
        for j in range(c2):
             row.append(0)
        result.append(row)       
#logic for matrix multiplication
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                result[i][j] += a[i][k] * b[k][j]
#display result
    print("resultant matrix: ")
    for r in result:
        print(r)

                
            





            





        
        
