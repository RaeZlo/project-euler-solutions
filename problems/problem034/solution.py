from math import factorial

def digit_factorial_sum(upper_bound: int = 1_000_000) -> int:
    # Precompute the factorials of digits 0–9
    digit_factorials = [factorial(i) for i in range(10)]

    total = 0
    for number in range(10, upper_bound + 1):
        if number == sum(digit_factorials[int(d)] for d in str(number)):
            total += number

    return total