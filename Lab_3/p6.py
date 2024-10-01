# 6. WAP to print sum of series 1 + 4 + 9 + 16 + 25 + 36 + ...n

# 1 * 1 = 1
# 2 * 2 = 4
# 3 * 3 = 9
# 4 * 4 =16
# etc....

no = int(input("Enter Number to print Series: "))

for i in range(1, no + 1):
    if i == 1:
        print(i, end=" ")
    else:
        print(f"{i*i}", end=" ")

print()
