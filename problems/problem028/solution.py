def number_spiral_diagonals(limit: int = 1001) -> int:
    if limit < 1 or limit % 2 == 0:
        raise ValueError('Limit must be a positive odd number.')

    diagonal_sum = 1  # Starting from the center
    for side_length in range(3, limit + 1, 2):
        # The four corners of each layer can be calculated as:
        # top-right = side_length ** 2
        # other corners decrease by (side_length - 1)
        corners_sum = 4 * (side_length ** 2) - 6 * (side_length - 1)
        diagonal_sum += corners_sum

    return diagonal_sum
