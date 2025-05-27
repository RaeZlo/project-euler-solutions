def get_first_n_digits_of_large_sum(numbers: list[int], n: int) -> str:
    total = sum(numbers)
    return  str(total)[:n]
