# 6. WAP to generate Fibonacci series of N given number using function name fibbo. (e.g. 0 1 1 2 3 5 8...)


def fibbo(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence


n = int(input("Enter a number: "))
fibonacci_series = fibbo(n)
print(f"Fibonacci series up to {n}: {fibonacci_series}")
