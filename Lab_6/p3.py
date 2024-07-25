# 3. WAP to find tuples that have all elements divisible by K from a list of tuples

tuples_list = [(10, 20, 30), (15, 25, 35), (12, 24, 36), (7, 14, 21)]

K = 5

result = []

for tup in tuples_list:
    divisible = True
    for element in tup:
        if element % K != 0:
            divisible = False
            break
    if divisible:
        result.append(tup)

print("Tuples where all elements are divisible by", K, ":", result)
