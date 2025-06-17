def custom_factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * custom_factorial(n-1)


def factorial_digit_sum(n: int) -> int:
    if not isinstance(n, int):
        raise TypeError('El valor ingresado debe ser un número entero.')
    if n < 0:
        raise ValueError('El valor ingresado no debe ser negativo.')
    
    factorial_result = custom_factorial(n)
    return sum(int(digit) for digit in str(factorial_result))
