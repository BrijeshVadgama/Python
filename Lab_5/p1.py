# 1. WAP to find sum of all the elements in List.

n = int(input("Enter How Many Elements Do You Want: "))
l1 = []
sum = 0

for i in range(1, n + 1):
    values = int(input(f"Enter Value {i}: "))
    l1.append(values)

for i in l1:
    sum += i
print(sum)
