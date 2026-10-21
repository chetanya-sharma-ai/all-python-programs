#program to print sum of series x+x2/2+x3/3....xn/n using for
x=int(input("enter the value of x= "))
n=int(input("enter the value of n= "))
i=1
sum=0
for i in range(i,n+1):
    sum=sum+pow(x,i)/i
    i=i+1
print("sum= ",sum)

    
