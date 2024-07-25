# 13. WAP to reverse an integer number using recursion.


def reverse_number(num, reversed_num=0):
    if num == 0:
        return reversed_num
    else:
        return reverse_number(num // 10, reversed_num * 10 + num % 10)


num = int(input("Enter a number: "))
result = reverse_number(abs(num))
if num < 0:
    result = -result
print(f"The reversed number is {result}")
