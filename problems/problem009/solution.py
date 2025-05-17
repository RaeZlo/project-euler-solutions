def find_pythagorean_triplet_product(total: int = 1000) -> int:
    for a in range(1, total):
        for b in range(a + 1, total - a):
            c = total - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1
