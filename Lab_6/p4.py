# 4. WAP to find Tuples with positive elements in List of tuples wihtout function

tuples_list = [(1, 2, -3), (1, 5, 6), (0, 7, 8), (9, -10, 11)]

result = []

for tup in tuples_list:
    all_positive = True
    for element in tup:
        if element <= 0:
            all_positive = False
            break
    if all_positive:
        result.append(tup)

print("Tuples with all positive elements:", result)
