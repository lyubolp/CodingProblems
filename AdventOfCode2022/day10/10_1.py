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

def cycle(actions: List[Tuple[str, int]]) -> List[int]:
    cycle = 0
    x = 1
    result = []

    for action in actions:
        if action[0] == 'noop':
            cycle += 1

            if cycle % 40 == 20:
                result.append(x * cycle)
        else:
            for i in range(2):
                cycle += 1

                if cycle % 40 == 20:
                    result.append(x * cycle)

            x += action[1]
    
    return result

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    commands = [split_input(input) for input in inputs]

    print(sum(cycle(commands)))