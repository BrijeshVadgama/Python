# 4. WAP that defines a function which returns 1 if the number is prime otherwise return 0.


def is_prime(num):
    if num <= 1:
        return 0
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return 0
    return 1


num = int(input("Enter a number: "))

result = is_prime(num)

if result == 1:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
