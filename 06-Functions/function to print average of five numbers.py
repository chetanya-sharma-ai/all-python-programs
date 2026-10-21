#function to find average of five numbers:

def avg(a,b,c,d,e):
    average=(a+b+c+d+e)/5
    return average

a=int(input("enter the value of first number: "))
b=int(input("enter the value of second number: "))
c=int(input("enter the value of third number: "))
d=int(input("enter the value of fourth number: "))
e=int(input("enter the value of fifth number: "))

result=avg(a,b,c,d,e)
print("average of numbers are: ",result)
