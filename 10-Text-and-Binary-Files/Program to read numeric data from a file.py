#Program to read numeric data from a file:
with open("numbers.txt","w")as file:
    file.write("10, 20 30 40 50 60")

with open("numbers.txt","r")as file:
    data=file.read()
    numbers=data.split

print("numbers in file")
for num in numbers:
    print(int(num))
    
