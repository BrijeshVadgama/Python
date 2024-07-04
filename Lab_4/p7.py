# 7. WAP to convert given array to string.

n = int(input("Enter how many elements do you want: "))
arr = []

for i in range(n):
    value = input(f"Enter Value {i+1}: ")
    arr.append(value)

str = arr
res = " ".join(arr)

print(f"\nArray Elements: {str}")
print("\nArray as a string:", res)
