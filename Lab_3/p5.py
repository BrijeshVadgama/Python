# 5. WAP to print sum of 1 to n numbers

no = int(input("Enter Number: "))
sum = 0
for i in range(1, no + 1):
    sum += i
print(f"Sum: {sum}")
