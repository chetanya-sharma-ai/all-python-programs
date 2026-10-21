#Program to check weather a string is pallindrome or not:
my_str=input("Enter a string: ")

#reverse a string and compare:
if my_str == my_str[::-1]:
    print("It is a pallindrome")
else:
    print("It is NOT a pallindrome")
