# 9. WAP to capitalize the first and last character of each word in a string.

str = input("Enter a string: ")
print(str)
str = str.title()
str = str.split()
string = ""
for i in str:
    string += i[:-1] + i[-1].upper() + " "
print(string)
