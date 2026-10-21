#create a file and wrtite contents:
with open("practice2.txt","w") as f:
    f.write("Hi my name is chetanya\nI am doing Btech\n")
    f.write("my specialization is aiml\nIam learning python.")

with open ("practice2.txt","r") as f:
    data=f.read()
print(data)
