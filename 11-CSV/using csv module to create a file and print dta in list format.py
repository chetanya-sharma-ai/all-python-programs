#using csv module create a file and print data inlist format:
import csv
#create and write to CSV file
with open('students.csv',"w",newline='') as f:
    writer=csv.writer(f)

    #writing header
    writer.writerow(["Roll", "Name","Class"])

    #writing data
    n=int(input("enter number of students"))
    for i in range(n):
        roll=input("enter roll no: ")
        name=input("enter Name: ")
        cls=input("enter class: ")

        writer.writerow([roll,name,cls])

print("\nData written successfully!\n")

#read and print CSV file contents
with open("Students.csv","r")as f:
    reader=csv.reader(f)

    print("CSV File Contents: ")
    for row in reader:
        print(row)
