def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    limit = int(n ** 0.5) + 1
    for i in range(3, limit, 2):
        if n % i == 0:
            return False
    return True

def find_nth_prime(target_index: int) -> int:
    count = 0
    number = 1

    while count < target_index:
        number += 1
        if is_prime(number):
            count += 1

    return number
