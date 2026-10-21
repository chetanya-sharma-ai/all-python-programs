#program to print sum of n natural no. using while
n=int(input("enter value of n= "))
i=1
sum=0
while i<=n:
    if(i%2!=0):
     sum=sum+i
    i=i+1
print("sum= ",sum)

