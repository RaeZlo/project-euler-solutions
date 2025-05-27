def collatz_length(n: int, cache: dict[int, int]) -> int:
    if n <= 0:
        raise ValueError('El número debe ser un entero positivo mayor que cero.')

    if n in cache:
        return cache[n]

    original_n = n
    length = 0

    while n != 1:
        if n in cache:
            length += cache[n]
            break
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        length += 1

    cache[original_n] = length + 1  # +1 incluye el número original
    return cache[original_n]


def find_longest_collatz(limit: int) -> int:
    max_length = 1
    starting_number = 1
    cache = {}

    for i in range(2, limit):
        length = collatz_length(i, cache)
        if length > max_length:
            max_length = length
            starting_number = i

    return starting_number
