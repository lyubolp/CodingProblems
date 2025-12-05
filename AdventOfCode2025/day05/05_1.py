import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> tuple[list[tuple[int, int]], list[int]]:
    ranges = [tuple(line.split("-")) for line in lines if "-" in line]
    ranges = [(int(start), int(end)) for (start, end) in ranges]
    items = [int(line) for line in lines if "-" not in line and line != ""]

    return ranges, items


def is_ingredient_fresh(ingredient: int, ranges: list[tuple[int, int]]) -> bool:
    return any(start <= ingredient <= end for (start, end) in ranges)


if __name__ == "__main__":
    lines = read_input()
    ranges, ingredients = parse_input(lines)
    print(ranges)
    print(ingredients)

    fresh_ingredients = [ingredient for ingredient in ingredients if is_ingredient_fresh(ingredient, ranges)]
    print(fresh_ingredients)
    print(len(fresh_ingredients))
