# 13. WAP to check whether the given number is palindrome or not

no = input("Enter Number to check whether it is palindrome or not: ")

rev = no[::-1]

if no == rev:
    print(f"{no} is Palindrome")
else:
    print(f"{no} is not Palindrome")
