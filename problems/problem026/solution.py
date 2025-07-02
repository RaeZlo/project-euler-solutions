def calculate_recurring_cycle_length(denominator: int) -> int:
    remainder_positions = {}
    numerator = 1
    position = 0

    while numerator != 0:
        if numerator in remainder_positions:
            return position - remainder_positions[numerator]
        
        remainder_positions[numerator] = position
        numerator = (numerator * 10) % denominator
        position += 1

    return 0  # Decimal exacto, sin ciclo


def find_denominator_with_longest_cycle(limit: int) -> int:
    max_length = 0
    best_denominator = 0

    for denominator in range(2, limit):
        cycle_length = calculate_recurring_cycle_length(denominator)
        
        if cycle_length > max_length:
            max_length = cycle_length
            best_denominator = denominator

    return best_denominator