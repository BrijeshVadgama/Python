# 6. WAP to count numbers of vowels in given string.

str = input("Enter a string: ")
count = 0

vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
count = 0
for char in str:
    if char in vowels:
        count += 1

print("Number of vowels in the given string:", count)
