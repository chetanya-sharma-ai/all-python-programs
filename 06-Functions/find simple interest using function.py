#function to print simple interest

def interest(p,r,t):
    simple_interest = (p*r*t)/100
    return simple_interest

p=int(input("entervalue of p: "))
r=int(input("enter the value of rate: "))
t=int(input("enter the value of time: "))

result=interest(p,r,t)
print("value of simple interest: ",result)
