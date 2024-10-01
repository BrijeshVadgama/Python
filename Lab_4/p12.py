# 12. WAP to check if a given string is binary string or not.

str = input("Enter a string: ")

is_binary = True

for char in str:
    if char not in {"0", "1"}:
        is_binary = False
        break

if is_binary:
    print(f"{str} is a binary string.")
else:
    print(f"{str} is not a binary string.")
