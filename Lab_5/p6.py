# 6.  WAP to reverses the list entered by user.

n = int(input("Enter how many elements you want: "))

l1 = []

for i in range(1, n + 1):
    values = int(input(f"Enter value {i}: "))
    l1.append(values)

rev = l1[::-1]

print(f"Original List: {l1}")
print(f"List After Reverse: {rev}")
