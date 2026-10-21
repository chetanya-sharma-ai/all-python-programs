#using csv module print data in proper format
import csv

with open('student.csv','r') as f:  
    reader = csv.reader(f)

    print("Roll No | Name | Class")
    print('-----------------------')
    for row in reader:
        print(row[0],"|",row[1],"|",row[2])
