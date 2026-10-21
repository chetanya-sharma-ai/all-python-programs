#Program to write and read a string from a file:
text=input("Enter a string: ")
file=open("dummy.txt","w")
file.write(text)
file.close()
print("Data written to file successfully")
file=open('dummy.txt','r')
data=file.read()
file.close()

print('Data read from file: ')
print(data)
