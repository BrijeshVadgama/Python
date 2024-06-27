# WAP to check whether the given year is leap year or not.
# [If a year can be divisible by 4 but not divisible by 100 then it is leap year but if it is divisible by 400 then it is leap year]


year = int(input("Enter Year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
