# 8. WAP to find out duplicate characters in given string.

str = input("Enter a string: ")
count = {}

for char in str:
    if char == " ":
        continue
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

print("Duplicate characters in the string:")
for char, count in count.items():
    if count > 1:
        print(f"{char}: {count}")
