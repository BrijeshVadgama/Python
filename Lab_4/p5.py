# 5. WAP to print even length word in string.

str = input("Enter a string: ")
words = str.split()
for word in words:
    if len(word) % 2 == 0:
        print(f"Even length word is: {word}")
