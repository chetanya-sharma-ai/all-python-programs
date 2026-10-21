#check weather a number is prime or not using foor loop
num=int(input("enter the number= "))
f=0
i=1
for i in range(i,num+1):
    if num%i==0:
        f=f+1
    i=i+1
if f==2:
    print("number is prime")
else:
    print("number is not prime")
