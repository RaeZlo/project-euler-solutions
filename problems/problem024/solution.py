from math import factorial

def find_nth_permutation(digits: list[str], n: int) -> str:
    total = factorial(len(digits))
    if not (1 <= n <= total):
        raise IndexError(f"n must be between 1 and {total}, got {n}")
    
    n -= 1
    available = sorted(digits)
    result = []

    for i in range(len(digits) - 1, -1, -1):
        f = factorial(i)
        index = n // f
        result.append(available.pop(index))
        n %= f

    return ''.join(result)
