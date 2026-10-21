#program with using return statement
def big(a,b):

    if a>=b:
        return a
    else:
        return b

a=int(input("enter first number: "))
b=int(input("enter the value of second number: "))

result=big(a,b)
print("maximum value: ",result)
