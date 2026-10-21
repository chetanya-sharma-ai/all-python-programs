#Program to open a file in binary mode:

f=open("dummy.txt","rb")
print("Name of file: ",f.name)
line=f.readline()
print("file contents are: ",line)
line=f.readline(5)
print("file conetents with readline(5) are: ",line)
f.close()
