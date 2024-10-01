# Extra-2: WAP to check whether last digit of number is divisible by 2 or not

no1 = int(input("Enter Number: "))
last = no1 % 10

if last != 0:
    if last % 2 == 0:
        print(f"{last} number is divisible by 2")
    else:
        print(f"{last} number is not divisible by 2")
else:
    print("Last Digit is Zero")
