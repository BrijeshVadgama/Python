# 11. WAP to calculate power of a number using recursion.


def power(base, exp):
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)


base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
result = power(base, exp)
print(f"{base} raised to the power of {exp} is {result}")
