#using csv module print data in list format
import csv
with open("student.csv","r",newline='')as f:
    reader=csv.reader(f)

    print('--------CSV DATA---------')
    for row in reader:
        print(row)
