# 3. WAP to remove ith character from given string.

s = input("Enter a string: ")
i = int(input("Enter the position (index start from 0): "))

new_str = s[:i] + s[i + 1 :]
print(f"The string after removing the character {i} is:, {new_str}")
