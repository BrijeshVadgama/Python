# 1. WAP to count simple interest using function.


def calculate_simple_interest(principal, rate, time):
    interest = (principal * rate * time) / 100
    return interest


principal = float(input("Enter Principal: "))

rate = float(input("Enter Rate of Interest: "))

time = float(input("Enter Time in Years: "))

result = calculate_simple_interest(principal, rate, time)

print(f"Simple Interest: {result}")
