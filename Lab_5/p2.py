# 2. WAP to find largest element in a List.

n = int(input("Enter How Many Elements Do You Want: "))
l1 = []

for i in range(1, n + 1):
    values = int(input(f"Enter Value {i}: "))
    l1.append(values)

max = l1[0]

for i in l1:
    if i > max:
        max = i

print(f"Largest Number in List is: {max}")
