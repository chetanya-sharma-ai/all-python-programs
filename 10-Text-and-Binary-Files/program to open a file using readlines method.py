#Program to open a file using readlines method:
f=open("dummy.txt","r")
print("Name of file: ",f.name)
line=f.readlines()
print('file conetents are: ',line)
f.close()
