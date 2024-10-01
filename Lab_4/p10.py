# 10. WAP to find Maximum frequency character in String.

str = input("Enter a string: ")
count = {}

for char in str:
    if char == " ":
        continue
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

max_freq = max(count.values())
max_freq_chars = [char for char, freq in count.items() if freq == max_freq]

for char in max_freq_chars:
    print(f"{char} : {max_freq}")
