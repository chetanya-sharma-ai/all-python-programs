#open a file in append mode and read the contents using read function:
f=open("demo3.txt","a")
print("name of the file: ",f.name)

#write a new line into the file:
str="There are two types of file:"
line=f.write(str)

#close file:
f.close()

#Open file again in read mode:
f=open("demo3.txt","r")
line=f.read()
print("file contents: ",line)

#close opened file again
f.close
