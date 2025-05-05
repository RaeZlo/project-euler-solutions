def sum_of_multiples(limit:int) -> int:
    """
    Calcula eficientemente la suma de todos los múltiplos de 3 o 5 menores que un número dado.

    Args:
        limit (int): Límite superior (exclusivo).

    Returns:
        int: Suma de todos los múltiplos de 3 o 5 menores que el límite.
    """
    return sum(num for num in range(limit) if num % 3 == 0 or num % 5 == 0)
