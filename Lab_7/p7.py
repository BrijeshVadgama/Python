# 7. WAP to find the factorial of a given number using recursion.


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


n = int(input("Enter a number: "))
result = factorial(n)
print(f"The factorial of {n} is {result}")
