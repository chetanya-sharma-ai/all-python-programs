#program to sort elements of a list(Bubble sort):
n=int(input("enter the value of n= "))
a=[]
for i in range(0,n):
    items=int(input("enter elements= "))
    a.append(items)
print("elements after sorting are= ")
for i in range(n):
    for j in range(0,n-i-1):
        if a[j]>a[j+1]:   #in case of descending use(<) in this line
            a[j],a[j+1]=a[j+1],a[j]

for i in range(len(a)):
    print(a[i])



