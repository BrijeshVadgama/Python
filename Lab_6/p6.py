# 6. WAP to convert binary tuple into integer.

binary_tuple = (1, 0, 1, 0, 1)

integer_value = 0

for bit in binary_tuple:
    integer_value = (integer_value << 1) | bit

print("Binary tuple converted to integer:", integer_value)
