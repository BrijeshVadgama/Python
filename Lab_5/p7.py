# 7. Python program to remove multiple elements from a list using list comprehension

n = int(input("Enter how many elements you want in the list: "))

lst = []

for i in range(n):
    value = int(input(f"Enter value {i + 1}: "))
    lst.append(value)

m = int(input("Enter how many elements you want to remove: "))

remove_lst = []
for i in range(m):
    value = int(input(f"Enter value to remove {i + 1}: "))
    remove_lst.append(value)

result_lst = [elem for elem in lst if elem not in remove_lst]

print(f"Original List: {lst}")
print(f"List after removing specified elements: {result_lst}")
