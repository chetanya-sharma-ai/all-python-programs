#program to open a file in read form using readline function:
f=open("dummy.txt","r")
print('Name of the file: ',f.name)
line=f.readline()
print("file contents are: ",line)
f.close()
