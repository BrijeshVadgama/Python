# WAP Calculate Area and Circumfrence of Circle

import math

radius = int(input("Enter Radius:: "))

result_area = math.pi * (radius**2)
result_circumfrence = 2 * math.pi * radius

print(f"Area Of Circle:= {result_area}")
print(f"Circumfrence Of Circle:= {result_circumfrence}")
