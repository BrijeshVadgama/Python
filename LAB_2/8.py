# WAP to calculate electricity bill based on following criteria. Which takes the unit from the user.
# a. First 1 to 50 units – Rs. 2.60/unit
# b. Next 50 to 100 units – Rs. 3.25/unit
# c. Next 100 to 200 units – Rs. 5.26/unit
# d. above 200 units – Rs. 8.45/unit

unit = float(input("Enter units: "))
bill = 0

if unit >= 1 and unit < 50:
    bill = unit * 2.60
elif unit >= 50 and unit < 100:
    bill = (50 * 2.60) + (unit - 50) * 3.25
elif unit >= 100 and unit <= 200:
    bill = (50 * 2.60) + (50 * 3.25) + (unit - 100) * 5.26
elif unit > 200:
    bill = (50 * 2.60) + (50 * 3.25) + (50 * 5.26) + (unit - 200) * 8.45

print(f"Bill is: {bill:.2f}")
