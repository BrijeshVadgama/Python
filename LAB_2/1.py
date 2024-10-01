# WAP to check whether the given number is positive or negative.

no = int(input("Enter Number: "))

if no > 0:
    print(f"{no} is positive")
elif no < 0:
    print(f"{no} is Negative")
else:
    print("Number is Zero")
