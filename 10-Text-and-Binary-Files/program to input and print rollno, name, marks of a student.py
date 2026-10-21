#program to inpput and print roll no name and percentageof studens and marks
#from five subjects:
f=open("student.txt","w")
n=int(input("Enter the number 0f students: "))
for i in range(n):
    roll=input("enter the roll number of student: ")
    name=input("Enter name of student: ")
    print("Enter the marks of five subjects respectively: ")
    m1=int(input("enter marks of subject1: "))
    m2=int(input("enter marks of subject2: "))
    m3=int(input("enter marks of subject3: "))
    m4=int(input("enter marks of subject4: "))
    m5=int(input("enter marks of subject5: "))
    f.write(f"(roll),(name),{m1},{m2},{m3},{m4},{m5}\n")
f.close()
f=open("student.txt","r")
print("\n Student details: \n")
for line in f:
    data=line.strip().split(",")
    roll=data[0]
    name=data[1]
    marks=list(map(int,data[2:]))
    total=sum(marks)
    percentage=total/5
    print("********************")
    print("Roll number: ",roll)
    print("name of student: ",name)
    print("marks obtained are: ",marks)
    print("total marks: ",total)
    print("percentage: ",percentage)
    print("*********************")
f.close()

    
    
    
    
    
