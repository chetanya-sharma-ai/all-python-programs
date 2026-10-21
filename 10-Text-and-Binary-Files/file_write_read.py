# Open a file in write mode and read the contents using read function
f = open("demo5.txt", "w")
print("Name of the file: ", f.name)
# Write a new line into the file
str = "Files are used to store data permanently. This file is chetanya sharma"
line = f.write( str )
# Close opened file
f.close()
# Open the file again in read mode
f = open("demo5.txt", "r")
line = f.read()
print("File Contents:\n", line)
# Close opened file again
f.close()
