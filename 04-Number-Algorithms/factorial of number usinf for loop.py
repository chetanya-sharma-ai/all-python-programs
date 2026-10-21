#program to find factorial using for loop
num=int(input("enter the value of a given number"))
if num>0:
    fact=1
    i=1
    for i in range(i,num+1):
        fact=fact*num
        num=num-1
    print("factorial of number is= ",fact)
else:
    print("error......")
    
