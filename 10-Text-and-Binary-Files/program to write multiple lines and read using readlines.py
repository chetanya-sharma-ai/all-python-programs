#program to write multiple lines and read using readline
lines=[]
n=int(input("enter no of lines: "))
for i in range(n):
    line=input("enter line: ")
    lines.append(line+"\n")
with open ("demo_2.txt","w")as file:
    file.writelines(lines)
print("Data written successfully")
with open ("demo_2.txt","r")as file:
    print("Reading file line by line:")

    while True:
        line=file.readline()
        if not line:
            break
    print(line,end="")
