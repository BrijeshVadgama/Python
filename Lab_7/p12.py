# 12. WAP to count digits of a number using recursion.


def count_digits(num):
    if num == 0:
        return 0
    else:
        return 1 + count_digits(num // 10)


num = int(input("Enter a number: "))
result = count_digits(abs(num))
print(f"The number of digits in {num} is {result}")
