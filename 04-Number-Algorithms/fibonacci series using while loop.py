#PROGRAM TO PRINT FIBONACCI SERIES:
n=int(input("enter value of n= "))
x=0
y=1
z=0
while(z<=n):
    print(z)
    x=y
    y=z
    z=x+y
    
