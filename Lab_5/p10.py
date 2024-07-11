# 10. WAP to count Even and Odd numbers in a List.

n = int(input("Enter how many elements you want in the list: "))

l1 = []

evenCount = 0
oddCount = 0

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    l1.append(value)

for i in l1:
    if i % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(f"Total Even Numbers into the List:: {evenCount}")
print(f"Total Odd Numbers into the List:: {oddCount}")
