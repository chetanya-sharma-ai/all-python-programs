#function to find area and perimeter

def area_rect(l,b):
    a=l*b
    p=2*(l+b)
    return a,p

length=int(input("enter the value of lenght: "))
breadth=int(input("enter the value of breadth: "))

area,perimeter=area_rect(length,breadth)

print("area of rectangle: ",area)
print("perimeter of rectangle: ",perimeter)
    
