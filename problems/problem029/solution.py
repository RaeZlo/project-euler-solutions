def distinct_powers(a_max: int = 100, b_max: int = 100) -> int:
    distinct_terms = {a ** b for a in range(2, a_max + 1) for b in range(2, b_max + 1)}
    return len(distinct_terms)
