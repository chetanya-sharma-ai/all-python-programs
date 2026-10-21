#program to print fabonacci series using a list
n=int(input("enter the numbers of fabonacci series required"))
a=0
b=1
c=0
list=[]
count=0
while count<n:
    list.append(a)
    count+=1
    c=a+b
    a=b
    b=c
