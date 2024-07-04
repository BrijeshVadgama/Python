# 4. WAP to find length of String without using len function.

str = input("Enter a string: ")
length = 0
for char in str:
    length += 1

print("Length of the string is:", length)
