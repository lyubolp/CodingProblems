import sys

from functools import reduce


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> list[list[str]]:
    return [line.split() for line in lines]


def evaluate_expression(expression: list[str]) -> int:
    operation = expression[-1]

    items = [int(item) for item in expression[:-1]]

    if operation == "+":
        return sum(items)
    elif operation == "*":
        return reduce(lambda acc, item: acc * item, items, 1)
    return 0


if __name__ == "__main__":
    lines = read_input()
    table = parse_input(lines)
    print(table)

    expressions = [[row[i] for row in table] for i, _ in enumerate(table[0])]
    print(expressions)

    result = 0
    for expression in expressions:
        current_result = evaluate_expression(expression)
        print(f" {expression[-1]} ".join(expression[:-1]), f" = {current_result}")
        result += current_result

    print(result)
