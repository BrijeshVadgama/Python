# 7. WAP to count frequency in list by dictionary.

my_list = [1, 2, 3, 4, 2, 1, 2, 5, 3, 2]

frequency_dict = {}

for item in my_list:
    if item in frequency_dict:
        frequency_dict[item] += 1
    else:
        frequency_dict[item] = 1

print("Frequency of elements in the list:")
for key, value in frequency_dict.items():
    print(f"{key}: {value}")
