# 7. WAP to print sum of series 1 – 2 + 3 – 4 + 5 – 6 + 7 ... n

# in odd print odd series and (+) sign
# in even print even series and (-) sign

no = int(input("Enter Number: "))

for i in range(1, no + 1):
    if i % 2 == 0:
        print(f"- {i}", end=" ")
    else:
        if i == 1:
            print(i, end=" ")
        else:
            print(f"+ {i}", end=" ")
