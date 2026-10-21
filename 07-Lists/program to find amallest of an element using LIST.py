#program to find smallest element from a list
n=int(input("enter the value of n= "))
a=[]
for i in range(0,n):
    items=int(input("enter elements= "))
    a.append(items)
    min=a[0]
for items in a[1:]:
    if(items<min):
        min=items
print("smallest number is= ",min)        
