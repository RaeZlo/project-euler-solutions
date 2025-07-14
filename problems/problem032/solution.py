def is_pandigital(s: str) -> bool:
    return len(s) == 9 and set(s) == set("123456789")


def generate_pandigital_products() -> set[int]:
    products = set()

    # Case 1: 1-digit × 4-digit = 4-digit
    for a in range(1, 10):
        for b in range(1234, 9877):
            product = a * b
            combined = f"{a}{b}{product}"
            if is_pandigital(combined):
                products.add(product)

    # Case 2: 2-digit × 3-digit = 4-digit
    for a in range(12, 100):
        for b in range(123, 988):
            product = a * b
            combined = f"{a}{b}{product}"
            if is_pandigital(combined):
                products.add(product)

    return products


def pandigital_products_sum() -> int:
    return sum(generate_pandigital_products())
