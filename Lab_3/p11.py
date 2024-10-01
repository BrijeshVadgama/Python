# 11. WAP to find whether the given number is prime or not.

no = int(input("Enter Number to check whether it is prime or not: "))

flag = True

if no <= 1:
    flag = False
else:
    for i in range(2, no):
        if no % i == 0:
            flag = False
            break

if flag:
    print(f"{no} is a Prime Number")
else:
    print(f"{no} is Not a Prime Number")
