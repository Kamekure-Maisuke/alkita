from cachetools import cached


@cached(cache={})
def fibonacci(n: int) -> int:
    match n:
        case 0 | 1:
            return n
        case _:
            return fibonacci(n - 2) + fibonacci(n - 1)


def create_star_line(total_width: int, stars: int) -> str:
    spaces = " " * (total_width - stars)
    star_string = "*" * stars
    return spaces + star_string


def generate_fibonacci_pattern(rows: int) -> str:
    if rows > 10:
        return ""
    pattern_lines = []
    for i in range(rows):
        stars = fibonacci(i)
        line = create_star_line(rows, stars)
        pattern_lines.append(line)

    return "\n".join(pattern_lines)
