def count_divisors(n: int) -> int:
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            if i == n // i:
                count += 1  # perfect square
            else:
                count += 2  # count both i and n // i
    return count


def first_triangular_with_divisors(min_divisors: int = 500) -> int:

    n = 1
    while True:
        triangular = n * (n + 1) // 2
        divisors = count_divisors(triangular)

        if divisors > min_divisors:
            return triangular

        n += 1
