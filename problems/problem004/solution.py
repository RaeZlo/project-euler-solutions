def is_palindrome(n: int) -> bool:
    s = str(n)
    return s == s[::-1]

def largest_palindrome_product(min_factor: int = 100, max_factor: int = 999) -> int:
    max_palindrome = 0

    for a in range(max_factor, min_factor - 1, -1):
        for b in range(a, min_factor - 1, -1):
            product = a * b
            if product <= max_palindrome:
                break
            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome
