#program to print sum of n odd no. using FOR LOOP
n=int(input("enter value of n= "))
i=1
sum=0
for i in range(i,n+1):
    if(i%2!=0):
     sum=sum+i
    i=i+1
print("sum= ",sum)

