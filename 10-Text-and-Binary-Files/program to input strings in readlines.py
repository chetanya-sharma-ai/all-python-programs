#Program to input strings in readlines:
n=int(input("Enter number of line: "))
with open("welcome.txt","w")as file:
    for i in range(n):
        line=input("enter line: ")
        file.write(line+"\n")
print("data written successfully: ")
with open("welcome.txt","r")as file:
    line=file.readlines()
print("\n Reading file using readlines(): ")
for line in lines:
    print(line,end=" ")
    
