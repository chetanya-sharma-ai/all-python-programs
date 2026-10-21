#use of seek and tell function

f=open("demo_3.txt","r")
print("current position of cursor is: ",f.tell())
f.seek(20)
print("current position of cursor is: ",f.tell())
line=f.read()
print("line:",line)
f.seek(2)
print("current position of cursor: ",f.tell())
line1=f.read()
print("line1=",line1)
