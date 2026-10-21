#list methods
fruits=["apple","banana","cherry"]
number=[10,34,90,10,45,49,10,34,3]
string1=['h','l','l','o']
number1=[90,5,71,50,12,6]
number2=[12,78,65,16,56]
print(fruits)
fruits.append("orange")
print("fruits")
print("number=",number)
print("number=",number.count(10))
number.extend([100,150])
print("number=",number)
print("index of 90=",number.index(90))
fruits.insert(1,"grapes")
print(fruits)
fruits.pop(0)
print(fruits)
number.remove(49)
print("number= ",number)
print("string1 =",string1)
string1.reverse()
print("string1 after reverse= ",string1)
print("number1=",number1)
number1.sort()
print("number1 list after sort in ascending order= ",number1)
number2.sort(reverse=True)
print("number1 list after sort in descending order= ",number2)
