#program to print factorial using iterative function:
def fact_iter(num):
    f=1
    for i in range(1,n+1):
        f=f*i
    return(f)
n=int(input("enter number to find factorial: "))
fact=fact_iter(n)
print("factorial of a number is ",fact)
