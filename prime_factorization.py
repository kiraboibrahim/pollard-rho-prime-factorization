import random


def gcd(a: int, b: int) -> int:
    if a == 0:
        return b
    if b == 0:
        return a
    return gcd(b, a % b)


def f(a: int, n: int, seed: int):
    return ((a * a) - seed) % n


def factorize(n: int):
    x = y = 2
    d = 1  # If the gcd is 1, then (x-y) and n are coprime
    seed = random.randint(2, n - 1)
    while d == 1 or d == n:
        x = f(x, n, seed)
        y = f(f(y, n, seed), n, seed)  # Move y twice as fast as x
        d = gcd(abs(x - y), n)
        if y == x:  # The function f() produces a cyclic sequence, a loop occurs if y overlaps x
            x = y = 2
            seed = random.randint(2, n - 1)
    return d


def is_prime(n: int) -> bool:
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorize(n: int) -> list[int]:
    if is_prime(n):
        return [n]
    elif n % 2 == 0:
        # Exhaust prime factors of 2 because the random seq generators tends to produce odd values
        return [2] + prime_factorize(n // 2)
    else:
        first_factor: int = factorize(n)
        second_factor: int = n // first_factor
        return sorted(prime_factorize(first_factor) + prime_factorize(second_factor))
