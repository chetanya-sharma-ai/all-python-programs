#function to print product of three numbers

def product(a,b,c):
    multiplication=a*b*c
    return multiplication

a=int(input("enter first number: "))
b=int(input("enter second number: "))
c=int(input("enter third number: "))

result=product(a,b,c)
print("final answer is: ",result)
