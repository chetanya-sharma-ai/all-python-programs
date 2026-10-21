#greater of three numbers using function without return:

a=int(input("enter a: "))
b=int(input("enter b: "))
c=int(input("enter c: "))

def big(a,b,c):
    if a>b:
        if a>c:
            print("a is big")
        else:
            print("c is big")
    else:
        if b>c:
            print("b is big")
        else:
            print("c is big")

big(a,b,c)
            
 

        
    
