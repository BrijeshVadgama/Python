# 12. WAP to print duplicates from a list of integers.

n = int(input("Enter how many elements you want in the list: "))

lst = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    lst.append(value)

element_count = {}

for element in lst:
    if element in element_count:
        element_count[element] += 1
    else:
        element_count[element] = 1

duplicates = [element for element, count in element_count.items() if count > 1]

print(f"Original List: {lst}")
print(f"Duplicate Elements: {duplicates}")
