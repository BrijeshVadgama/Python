# 4. WAP to print numbers between two given numbers which is divisible by 2 but not divisible by 3

no1 = int(input("Enter Number 1: "))
no2 = int(input("Enter Number 2: "))

for i in range(no1, no2 + 1):
    if i % 2 == 0 and i % 3 != 0:
        print(i)
