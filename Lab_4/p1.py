# 1. WAP to check given string is palindrome or not.

str = input("Enter a string: ")
rev = str[::-1]

if str == rev:
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")
