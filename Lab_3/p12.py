# 12. WAP to print sum of digits of given number

no = int(input("Enter Number: "))

sum = 0

while no > 0:
    digit = no % 10
    no //= 10
    sum += digit

print(f"Sum of Digits: {sum}")
