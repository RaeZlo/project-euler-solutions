def sum_square_difference(n: int) -> int:
    sum_of_squares = sum([i ** 2 for i in range(n + 1)])
    square_of_sum = sum([i for i in range(n + 1)]) ** 2
    
    return square_of_sum - sum_of_squares
