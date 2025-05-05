def sum_even_fibonacci(limit: int) -> int:
    previous, current = 1, 2
    even_sum = 0

    while current <= limit:
        if current % 2 == 0:
            even_sum += current
        previous, current = current, previous + current

    return even_sum
