# WAP to calculate simple interest.

P = int(input("Enter Principle: "))
R = int(input("Enter Rate Of Interest: "))
N = int(input("Enter No Of Years: "))

result = (P * R * N) / 100

print(f"Simple Interest:= {result}")
