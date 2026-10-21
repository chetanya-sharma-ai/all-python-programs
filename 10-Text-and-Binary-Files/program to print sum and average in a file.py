#program to print sum and average in a file:
with open("num.txt","w")as file:
    n=(input("Enter numbers using spacing"))
    file.write(n)

with open("num.txt","r")as file:
    data=file.read()
    numbers=data.split()

numbers=[int(num)for num in numbers]

total=sum(numbers)
average=total/len(numbers)

print('numbers',numbers)
print('total sum of numbers are: ',total)
print("average of numbers are: ",average)
