#program to find smaller of three numbers using nested-if statement
a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

if a<b:
    if a<c:
     print("a is small")
    else:
     print("c is small")
else:
    if b<c:
        print("b is small")
    else:
        print("c is small")
        
