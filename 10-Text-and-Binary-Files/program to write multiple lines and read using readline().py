#Program to write multiple lines and read using readline():

lines=[]
n=int(input("Enter the number of lines: "))
for i in range(n):
    line=input("Enter line: ")
    lines.append(line+ \n)

with open("Hello.txt","w")as file:
    file.writelines(lines)
print("Data written successfully")

with open("Hello.txt","r")as file:
    print("Reading file line by line: ")

    while True:
        line=file.readline()
        if not line:
            break
        print(line,end="  ")
