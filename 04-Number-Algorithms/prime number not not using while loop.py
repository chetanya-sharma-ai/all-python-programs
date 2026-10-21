#program to check weather a number is prime or not using while loop
num=int(input("enter the number= "))
f=0
i=1
while i<=num:
    if num%i==0:
        f=f+1
    i=i+1
if f==2:
    print("number is prime")
else:
    print("number is not  prime")
    
    
