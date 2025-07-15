from math import gcd

def is_digit_cancelling(numerator: int, denominator: int) -> bool:
    if numerator >= denominator:
        return False  # Debe ser una fracción propia

    n_str, d_str = str(numerator), str(denominator)
    
    # Buscar dígitos comunes no cero
    for digit in n_str:
        if digit in d_str and digit != '0':
            # Cancelamos el dígito común
            n_new = n_str.replace(digit, '', 1)
            d_new = d_str.replace(digit, '', 1)
            # Validamos que la fracción "cancelada" sea válida
            if n_new and d_new and d_new != '0':
                if int(d_new) != 0:
                    try:
                        original = numerator / denominator
                        cancelled = int(n_new) / int(d_new)
                        if abs(original - cancelled) < 1e-9:
                            return True
                    except ZeroDivisionError:
                        continue
    return False

def solve() -> int:
    num_product = 1
    den_product = 1

    for num in range(10, 100):
        for den in range(10, 100):
            if is_digit_cancelling(num, den):
                num_product *= num
                den_product *= den

    # Simplificamos la fracción resultante
    common = gcd(num_product, den_product)
    return den_product // common
