# WAP to check whether the given number is odd or even

no = int(input("Enter Number: "))

if no % 10 == 0:
    print(f"{no} is Even Number.")
else:
    print(f"{no} is Odd Number.")
