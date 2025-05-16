def greatest_product_in_series(series: str, length: int) -> int:
    max_product = 0

    for i in range(len(series) - length + 1):
        substring = series[i:i + length]

        if '0' in substring:
            continue

        product = 1
        for digit in substring:
            product *= int(digit)

        if product > max_product:
            max_product = product

    return max_product