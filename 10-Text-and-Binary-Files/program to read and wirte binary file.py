#program to write and read data from binary file:
data="binary file store data"

with open("abc.bin","wb") as file:
    file.write(data.encode())
    
print('Data written successfully')

with open("abc.bin","rb") as file:
    read_data=file.read()
print("Data in file=\n",read_data.decode())




