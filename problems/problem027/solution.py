def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_quadratic_coefficients_with_max_primes(a_limit: int = 1000, b_limit: int = 1000) -> int:
    max_primes = 0
    product_of_coefficients = 0

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = 0
            while is_prime(n**2 + a*n + b):
                n += 1
            if n > max_primes:
                max_primes = n
                product_of_coefficients = a * b

    return product_of_coefficients