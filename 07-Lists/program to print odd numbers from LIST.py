#program to print odd numbers from n list elements
n=int(input("enter the value of n= "))
a=[]
for i in range(0,n):
    items=int(input("enter the elements= "))
    a.append(items)
print("odd numbers are= ")
for i in range(len(a)):
    if(a[i]%2!=0):
        print(a[i])
