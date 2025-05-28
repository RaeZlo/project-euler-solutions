def binomial_coefficient(n: int, k: int) -> int:
    if not 0 <= k <= n:
        return 0
    
    numerator = 1
    denominator = 1

    for i in range(1, k+1):
        numerator *= n - (i - 1)
        denominator *= i
    return numerator // denominator