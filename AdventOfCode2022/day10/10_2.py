import os
import sys

from typing import Dict, List, Tuple


def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input(input: str) -> Tuple[str, int]:
    if input.find(' ') != -1:
        command = input.split()
        return command[0], int(command[1])
    else:
        return input, None

def cycle(actions: List[Tuple[str, int]]) -> List[str]:
    cycle = 0
    x = 1
    result = []
    current_symbol = 0

    for action in actions:         
        if action[0] == 'noop':
            max_range = 1
        else:
            max_range = 2
                            
        for i in range(max_range):

            target_symbol = '#' if x - 1 <= current_symbol <= x + 1 else '.'
            result.append(target_symbol)
            current_symbol += 1
            cycle += 1

            if current_symbol >= 40:
                current_symbol -= 40

        if action[0] == 'addx':
            x += action[1]

    return result


def convert_1d_to_2d(items: List[str], rows: int, cols: int) -> List[List[str]]:
    result = []

    for i in range(rows):
        result.append(items[:cols])
        items = items[cols:]

    return result


if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    commands = [split_input(input) for input in inputs]
    result = cycle(commands)

    result_2d = convert_1d_to_2d(result, 6, 40)

    for row in result_2d:
        print(' '.join(row))