def find_fibonacci_index_with_digits(digits: int) -> int:
    if digits <= 1:
        return 1
    
    previous, current = 1, 1
    index = 2 

    while len(str(current)) < digits:
        previous, current = current, previous + current
        index += 1

    return index
