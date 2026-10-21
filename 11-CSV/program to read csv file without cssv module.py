#without csv module print data ina file
f=open("student.csv","r")
print("---------CSV DATA---------")
for line in f:
    data=line.strip().split(",")
    print(data)
f.close()
