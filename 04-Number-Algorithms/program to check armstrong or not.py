#Program to check weather a number is armstrong or NOT:

num=int(input("Enter a number: "))
n=num
power=len(str(num))
total=0

while n>0:
    digit=n%10
    total=total+digit**power
    n=n//10

if total==num:
    print("Entered number is armstrong")
else:
    print("Entered number is not armstrong")
