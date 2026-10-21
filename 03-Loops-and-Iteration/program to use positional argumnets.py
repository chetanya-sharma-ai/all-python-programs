#program to use positional arguments

def demo(rollno, name , fees):
    print("roll number: ",rollno)
    print("name: ",name)
    print("fees: ",fees)

rollno=int(input("enter rollno: "))
name=str(input("enter your name: "))
fees=float(input("enter your fees: "))

demo(rollno,name,fees)   
