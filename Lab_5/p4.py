# 4. WAP to interchange first and last elements in list entered by a user.

n = int(input("Enter how many elements you want: "))

l1 = []

for i in range(1, n + 1):
    values = int(input(f"Enter value {i}: "))
    l1.append(values)

if len(l1):
    l1[0], l1[-1] = l1[-1], l1[0]

print(f"List after interchanging elements: {l1}")
