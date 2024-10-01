# 2. WAP that defines a function to add first n numbers.


def add_numbers(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


n = int(input("Enter a number: "))
sum = add_numbers(n)
print(f"The sum of first {n} numbers is: {sum}")
