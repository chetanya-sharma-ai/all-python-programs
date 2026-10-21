#program to find greatest of three numbers using return statement:

def big(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
a=int(input("enter value of first number: "))
b=int(input("enter value of second number: "))
c=int(input("enter value of third number: ")) 

result=big(a,b,c)
print("greatest number is: ",result)
