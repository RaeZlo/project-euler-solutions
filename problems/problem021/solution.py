def divisors_sum(num: int) -> int:
    if num < 2:
        return 0
    total = 1
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            total += i
            if i != num // i:
                total += num // i
    return total

def amicable_numbers(limit: int = 10_000) -> int:
    result = 0
    for i in range(1, limit):
        a = divisors_sum(i)
        b = divisors_sum(a)
        if b == i and i != a:
            result += i
    return result