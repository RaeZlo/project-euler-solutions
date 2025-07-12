def digit_fifth_powers(power: int = 5) -> int:
    if power < 1:
        return 0
    
    digit_power = {str(d): d**power for d in range(10)}
    search_limit = (9 ** power) * power

    results = [i for i in range(2, search_limit) if i == sum(digit_power[d] for d in str(i))]
    return sum(results)
