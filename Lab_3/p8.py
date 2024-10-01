# 8. WAP to print multiplication table of given number.

no = int(input("Enter Number to Print Multiplication Table: "))

for i in range(1, 11):
    print(f"{no} * {i} = {no * i}")
