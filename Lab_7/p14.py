# 14. WAP to convert decimal number into binary using recursion.


def decimal_to_binary(n):
    if n == 0:
        return ""
    else:
        return decimal_to_binary(n // 2) + str(n % 2)


num = int(input("Enter a decimal number: "))
if num == 0:
    result = "0"
else:
    result = decimal_to_binary(num)
print(f"The binary representation of {num} is {result}")
