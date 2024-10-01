# 11. Python program to find N largest and smallest elements from the list

ele = int(input("Enter the number of elements in the list: "))

l1 = []

for i in range(ele):
    element = int(input(f"Enter element {i+1}: "))
    l1.append(element)

n = int(input("Enter the number of elements to find: "))

if n > len(l1):
    print("N is larger than the list length.")
else:
    sorted_l1_desc = sorted(l1, reverse=True)
    n_largest = sorted_l1_desc[:n]

    sorted_l1_asc = sorted(l1)
    n_smallest = sorted_l1_asc[:n]

    print(f"The {n} largest elements are: {n_largest}")
    print(f"The {n} smallest elements are: {n_smallest}")
