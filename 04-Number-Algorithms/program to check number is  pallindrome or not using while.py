#Program to check weather a number is pallindrome or not:
x=int(input("Enter the value of n: "))
sum=0
xcopy=x
while xcopy>0:
    sum=sum*10
    sum=sum+(xcopy%10)
    xcopy=xcopy//10
if x==sum:
    print("Number is a Pallindrome")
else:
    print("Number is NOT Pallindrome")
    
