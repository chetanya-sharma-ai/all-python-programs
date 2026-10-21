#program to find factorial of a given number
num= int(input("enter a number to calculate factorial= "))
if num>0:
    fact=1
    i=1
    while i<=num:
        fact=fact*num
        num=num-1
    print("factorial of a given number= ",fact)
else:
    print("error!!!!, number entered is negative.....")
    
