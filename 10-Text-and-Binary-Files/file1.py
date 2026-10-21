#open a file in write mode and read the contents using read function:
f=open("demo5.txt","w")
print("Name of the title: ",f.name)

#write a new line into file:
str="files are used to perform data: "
line=f.write(str)

#close file
f.close()

#open file again in read mode:
f=open("demo5.txt","r")
line=f.read()
print("contents of the file\n",line)

#close:
f.close()
