# WAP to implement simple calculator which performs (add,sub,mul,div) of two no. based on user input.

no1 = int(input("Enter Number 1: "))
no2 = int(input("Enter Number 2: "))

print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choice = int(input("Enter Your Choice: "))

print("---------- Using If Else ----------")

if choice == 1:
    print(f"Addition is: {no1 + no2}")
elif choice == 2:
    print(f"Subtraction is: {no1 - no2}")
elif choice == 3:
    print(f"Multiplication is: {no1 * no2}")
elif choice == 4:
    if no2 == 0:
        print("\nCannot Divide By Zero")
    else:
        print(f"Division is: {no1 / no2}")
else:
    print("Invalid Choice")

print("---------- Using Match Case ----------")

match choice:
    case 1:
        print(f"Addition is: {no1 + no2}")
    case 2:
        print(f"Subtraction is: {no1 - no2}")
    case 3:
        print(f"Multiplication is: {no1 * no2}")
    case 4:
        if no2 == 0:
            print("\nERROR! - Cannot Divide By Zero")
        else:
            print(f"Division is: {no1 / no2}")
    case _:
        print("Invalid Choice")
