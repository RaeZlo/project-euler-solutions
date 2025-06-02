def power_digit_sum(base: int = 2, exponent: int = 1000) -> int:
    if not isinstance(base, int) or not isinstance(exponent, int):
        raise TypeError('Tanto la base como el exponente deben ser enteros.')

    number = base ** exponent
    return sum(int(digit) for digit in str(abs(number)))
