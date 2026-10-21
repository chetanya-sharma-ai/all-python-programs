#using calculator module

from calculator import *
a=eval(input("enter number a: "))
b=eval(input("enter number b: "))
add=sum(a,b)
print("sum of two numbers is: ",add)
minus=subtract(a,b)
print("difference of two number: ",minus)
division=divide(a,b)
print("division of two number: ",division)
remaind=remainder(a,b)
print("remainder after division of numbers: ",remaind)
