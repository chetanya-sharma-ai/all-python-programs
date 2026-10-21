#program to swapno. using function:
a=int(input("enter a: "))
b=int(input("enter b: "))
def swap(a,b):
    temp=a
    a=b
    b=temp
    print("after swapping a= ",a)
    print("after swapping b= ",b)
swap(a,b)    
