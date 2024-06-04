# WAP to print Multiplication table of given number.

num = int(input("Enter Number to Print Table:: "))

for i in range(1, 11):
    print(f"{num} * {i} = {num*i}")

# # print table in range

# start = int(input("Enter Start Value:: "))
# end = int(input("Enter End Value:: "))

# for i in range(start, end + 1):
#     print(f"\nTable {i}")
#     for j in range(1, 11):
#         print(f"{i} * {j} = {i*j}")
