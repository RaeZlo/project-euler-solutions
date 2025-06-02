NUM_WORDS = {
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
    6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten',
    11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen',
    20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
    60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety',
    1000: 'one thousand'
}

def count_letter_length(number: int, words_map: dict[int, str]) -> int:
    if not (1 <= number <= 1000):
        raise ValueError('El número debe estar entre 1 y 1000 inclusive.')
    
    if number in words_map:
        return len(words_map[number].replace(" ", ""))
    
    if number < 100:
        tens = (number // 10) * 10
        units = number % 10
        return len(words_map[tens]) + len(words_map[units])
    
    if number < 1000:
        hundreds = number // 100
        remainder = number % 100
        letter_count = len(words_map[hundreds]) + len("hundred")

        if remainder:
            letter_count += len("and") + count_letter_length(remainder, words_map)

        return letter_count

    return 0


def total_letter_count(limit: int = 1000) -> int:
    return sum(count_letter_length(i, NUM_WORDS) for i in range(1, limit + 1))
