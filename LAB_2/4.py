# WAP to find out largest number from given three numbers.

no1 = int(input("Enter Number 1: "))
no2 = int(input("Enter Number 2: "))
no3 = int(input("Enter Number 3: "))

if no1 > no2:
    if no1 > no3:
        print(f"{no1} is largest")
    else:
        print(f"{no3} is largest")
else:
    if no2 > no3:
        print(f"{no2} is largest")
    else:
        print(f"{no3} is largest")
