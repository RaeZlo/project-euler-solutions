LIMIT = 28123

def sum_of_proper_divisors(n: int) -> int:
    if n < 2:
        return 0
    total = 1
    sqrt_n = int(n**0.5) + 1
    for i in range(2, sqrt_n):
        if n % i == 0:
            total += i
            complement = n // i
            if complement != i:
                total += complement
    return total

def is_abundant(n: int) -> bool:
    return sum_of_proper_divisors(n) > n

def solve() -> int:
    # Paso 1: Generar todos los abundantes hasta el límite
    abundants = [i for i in range(1, LIMIT + 1) if is_abundant(i)]

    # Paso 2: Marcar todos los números que pueden ser suma de dos abundantes
    can_be_written = [False] * (LIMIT + 1)
    for i in abundants:
        for j in abundants:
            suma = i + j
            if suma > LIMIT:
                break
            can_be_written[suma] = True

    # Paso 3: Sumar los que no pueden ser escritos como suma de dos abundantes
    return sum(i for i, can_be in enumerate(can_be_written) if not can_be)
