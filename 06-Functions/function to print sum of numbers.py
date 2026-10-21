#program to print sum of five numbers using function

def sum1(a,b,c,d,e):
    add=a+b+c+d+e
    return add
a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))
d=int(input("enter d: "))
e=int(input("enter e: "))

result=sum1(a,b,c,d,e)
print("result",result)
