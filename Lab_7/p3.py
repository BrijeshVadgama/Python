# 3. WAP to find maximum number from given two numbers using function


def find_max(a, b):
    return a if a > b else b


# Test the function

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

max_num = find_max(num1, num2)
print(f"The maximum number is: {max_num}")
