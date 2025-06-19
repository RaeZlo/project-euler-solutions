def load_and_sort_names(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        content = file.read()

    # Elimina comillas y divide los nombres
    names = [name.strip('"') for name in content.split(',') if name.strip('"')]
    return sorted(names)


def alphabetical_value(name: str) -> int:
    return sum(ord(char) - 64 for char in name.upper())


def total_name_scores(filepath: str = 'problems/problem022/names.txt') -> int:
    names = load_and_sort_names('problems/problem022/names.txt')
    return sum(alphabetical_value(name) * position for position, name in enumerate(names, start=1))
