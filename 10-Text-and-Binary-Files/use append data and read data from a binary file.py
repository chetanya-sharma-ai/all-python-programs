#program to use append data and read data from a binary file;
data=b"speed of binary file is fast"
with open ("abcd.bin",'ab') as file:
    file.write(data)

print("Data appended successfully")

with open('abcd.bin','rb') as file:
    read_data=file.read()

print("Data in file=\n",read_data)
