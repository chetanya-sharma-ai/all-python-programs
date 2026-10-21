#program to print sum of series x+x2/2+x3/3....xn/n using while
x=int(input("enter the value of x= "))
n=int(input("enter the value of n= "))
i=1
sum=0
while i<=n:
    sum=sum+pow(x,i)/i
    i=i+1
print("sum= ",sum)

    
