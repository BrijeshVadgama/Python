# 5. Write a function called primes that takes an integer value as an argument and returns a list of all prime numbers up to that number.


def primes(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    prime_list = []
    for num in range(2, n + 1):
        if is_prime(num):
            prime_list.append(num)

    return prime_list


n = int(input("Enter a number: "))
prime_numbers = primes(n)
print(f"Prime numbers up to {n}: {prime_numbers}")
