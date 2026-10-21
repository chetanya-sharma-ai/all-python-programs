#Print factorial using recursion:
def rec_fact(n):
    if n==0:
        return 1
    else:
        return n*rec_fact(n-1)

n=int(input("Enter number whose factorial is to be found: "))
fact=1
fact=rec_fact(n)
print("Factorial of number: ",fact)
        
