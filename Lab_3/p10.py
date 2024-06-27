# 10. WAP to find factors of the given number

no = int(input("Enter Number: "))

for i in range(1, no + 1):
    if no % i == 0:
        print(i)
