#create a file and writing contents into it:
with open ("practice.txt","w") as f:
    f.write("Hi everyone\nWe are learning file I/O\n")
    f.write("Using JAVA.\nI like programming in JAVA.")

with open ("practice.txt","r") as f:
    data=f.read()
    
new_data = data.replace("JAVA","Python")
print(new_data)

with open("practice.txt","w")as f:
    f.write(new_data)

    
