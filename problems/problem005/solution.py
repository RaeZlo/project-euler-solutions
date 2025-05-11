from math import gcd
from functools import reduce

def lcm(a: int, b: int) -> int:
    """
    Calcula el mínimo común múltiplo (MCM) de dos números enteros.

    Args:
        a (int): Primer número.
        b (int): Segundo número.

    Returns:
        int: El MCM de a y b.
    """
    return abs(a * b) // gcd(a, b)

def smallest_multiple(limit: int) -> int:
    """
    Calcula el número más pequeño divisible por todos los números desde 1 hasta `limit`.

    Args:
        limit (int): Límite superior del rango (incluido).

    Returns:
        int: El menor múltiplo común de todos los números en el rango.
    """
    if limit <= 0:
        return 0
    
    return reduce(lcm, range(1, limit + 1))
