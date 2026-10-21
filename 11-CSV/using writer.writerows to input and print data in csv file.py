#using writer.writerows to input and print the data
import csv
rows=[]
n=int(input("Enter numeber of records: "))
rows.append(["Roll No ","Name ","class "])

for i in range(n):
    roll=input("enter roll no: ")
    name=input("enter name of student: ")
    cls=input("enter class: ")

    rows.append([roll,name,cls])

with open('data.csv',"w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(rows)

with open("data.csv","r") as file:
    reader=csv.reader(file)

    print("\nFile content: ")
    for row in reader:
        print(row)
