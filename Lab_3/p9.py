# 9. WAP to find factorial of the given number

no = int(input("Enter Number to Find Factorial: "))
fact = 1
for i in range(1, no + 1):
    fact *= i
print(f"Factorial: {fact}")
