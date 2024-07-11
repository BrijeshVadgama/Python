# 5. WAP to interchange the elements on two positions entered by a user.

n = int(input("Enter how many elements you want: "))

l1 = []

for i in range(1, n + 1):
    values = int(input(f"Enter value {i}: "))
    l1.append(values)

pos1 = int(input("Enter the first position to interchange: ")) - 1
pos2 = int(input("Enter the second position to interchange: ")) - 1

if pos1 < 0 or pos1 >= n or pos2 < 0 or pos2 >= n:
    print("Invalid positions entered. Please enter valid positions.")
else:
    l1[pos1], l1[pos2] = l1[pos2], l1[pos1]

print(f"List after interchanging elements at positions {pos1 + 1} and {pos2 + 1}: {l1}")
