# 8. Create a list from the specified start to end index of another list.

n = int(input("Enter how many elements you want in the list: "))

l1 = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    l1.append(value)

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))

if start_index < 0 or end_index >= n or start_index > end_index:
    print("Invalid indices entered. Please enter valid indices.")
else:
    sublist = l1[start_index : end_index + 1]

    print(f"Original List: {l1}")
    print(f"Sublist from index {start_index} to {end_index}: {sublist}")
