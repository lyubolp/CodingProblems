import sys
from functools import reduce

def read_input() -> list[str]:
    return [line for line in sys.stdin]


def split_input(lines: list[str]) -> tuple[list[str], list[str]]:
    for i, line in enumerate(lines):
        if line == '\n':
            return lines[:i], lines[i+1:]

    raise ValueError("Invalid input")

def parse_stacks(stack_lines: list[str]) -> list[list[str]]:
    columns = [pos for pos, char in enumerate(stack_lines[-1]) if char.isdigit()]

    return [parse_stack_line_column(stack_lines, column) for column in columns]


def parse_stack_line_column(stack_lines: list[str], column) -> list[str]:
    return [item for line in stack_lines[:-1] if (item := line[column].strip()) != '']


def parse_move_lines(lines: list[str]) -> list[tuple[int, int, int]]:
    return [parse_move_line(line) for line in lines]


def parse_move_line(line: str) -> tuple[int, int, int]:
    line = line.strip().split()

    return int(line[1]), int(line[3]), int(line[5])


def execute_move(stacks: list[list[str]], move: tuple[int, int, int]) -> list[list[str]]:
    amount, from_, to = move

    items = stacks[from_-1][:amount]
    stacks[from_-1] = stacks[from_-1][amount:]
    stacks[to-1] = items + stacks[to-1]

    return stacks

if __name__ == "__main__":
    inputs = [user_input for user_input in read_input()]
    stack_lines, move_lines = split_input(inputs)

    stacks = parse_stacks(stack_lines)
    moves = parse_move_lines(move_lines)

    stacks = reduce(execute_move, moves, stacks)


    print(''.join(stack[0] for stack in stacks))
