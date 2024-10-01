# Extra-1: WAP to check roots of ax^2+bx+c

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

d = (b * b) - (4 * a * c)
d = d**0.5  # root
print(f"d: {d}")
if d == 0:
    root = (-b + d) / (2 * a)
    print(f"root is: {root}")
else:
    root1 = (-b + d) / (2 * a)
    root2 = (-b - d) / (2 * a)
    print(f"root1: {root1}\nroot2: {root2}")
