#PROGRAM TO PRINT REVERSE OF A NUMBER
x=int(input("enter the value of n= "))
print("digits of no. after reverse= ")
while x>0:
    y=x%10
    print(y, end="")
    x=x//10
    
