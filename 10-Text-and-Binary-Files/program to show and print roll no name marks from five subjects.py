#program to show and print roll no, name, marks,from five subjects:
f=open("student10.txt","w")
n=int(input("enter numebr of students: "))
for i in range(n):
    roll=input("enter roll no: ")
    name=input("enter name of the students: ")
    print("Enter the marks of five subjects: ")
    n1=int(input("Subject1: "))
    n2=int(input("Subject2: "))
    n3=int(input("Subject3: "))
    n4=int(input("Subject4: "))
    n5=int(input("Subject4: "))
    f.write(f"(roll),(name),{n1},{n2},{n3},{n4},{n5}\n")
f.close()

f=open("student10.txt","r")
print("\nStudent details:\n")

for line in f:
    data=line.strip().split(",")
    roll=data[0]
    name=data[1]
    marks=list(map(int,data[2:]))
    total=sum(marks)
    percentage=total/5
    print("Roll no",roll)
    print("name of student: ",name)
    print("marks obtained: ",marks)
    print("total: ",total)
f.close()

    
