# 3. WAP to print odd numbers between 1 to n

no = int(input("Enter Number: "))

for i in range(1, no + 1):
    if i % 2 != 0:
        print(i)
