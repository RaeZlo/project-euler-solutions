def is_prime(n: int) -> int:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def sum_prime(num: int) -> int:
    number = 0
    for i in range(num):
        if is_prime(i):
            number += i
    return number
