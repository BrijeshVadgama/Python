# 11. WAP to find Minimum frequency character in String.

str = input("Enter a string: ")
count = {}

for char in str:
    if char == " ":
        continue
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

min_freq = min(count.values())
min_freq_chars = [char for char, freq in count.items() if freq == min_freq]

for char in min_freq_chars:
    print(f"{char} : {min_freq}")
