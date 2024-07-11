# 3. WAP to split the List into two and append the first part to the end.

n = int(input("Enter how many elements you want: "))

l1 = []

for i in range(1, n + 1):
    values = int(input(f"Enter value {i}: "))
    l1.append(values)

split = len(l1) // 2

first_part = []
second_part = []

for i in range(len(l1)):
    if i < split:
        first_part.append(l1[i])
    else:
        second_part.append(l1[i])

res = second_part + first_part

print(f"Original List: {l1}")
print(f"List After Modification: {res}")
