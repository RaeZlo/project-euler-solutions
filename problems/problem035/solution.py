def is_prime(num: int) -> bool:
    if num < 2:
        return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True

def list_primes(limit: int) -> list[int]:
    return [i for i in range(2, limit) if is_prime(i)]

def get_rotations(num: int) -> list[int]:
    s = str(num)
    return [int(s[i:] + s[:i]) for i in range(len(s))]

def circular_primes(limit: int = 1_000_000) -> int:
    primes = set(list_primes(limit))
    result = 0

    for i in range(2, limit):
        if i in primes:
            rotations = get_rotations(i)
            if all(r in primes for r in rotations):
                result += 1
    return result
