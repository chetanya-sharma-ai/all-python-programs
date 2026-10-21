#program to swap numbers using return statement in function:

defswap(a,b):
    return(b,a)

a=int(input("enter the value of number1: "))
b=int(input("enter the value of number2: "))

x,y=swap(a,b)

print("after swapping: ")
print("first number: ",x)
print("second number: ",y)

