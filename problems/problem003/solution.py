def largest_prime_factor(target:int) -> int:
    divisor = 2
    factors = []

    while divisor <= target:
        if target % divisor == 0:
            factors.append(divisor)
            target //= divisor
        else:
            divisor += 1 if divisor == 2 else 2
    
    return max(factors)
