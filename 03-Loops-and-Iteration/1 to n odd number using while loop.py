#program to print 1 to n even numbers using while loop
n=int(input("enter value of n"))
i=1
while i<=n:
    if(i%2!=0):
        print(i,end="  ")
    i=i+1
