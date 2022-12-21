import sys

from collections import namedtuple
from enum import Enum
from typing import Dict, List, Tuple, Callable, Union, Optional, Set


Operation = namedtuple('Operation', ['op', 'arg1', 'arg2'])

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def parse_input(input: str) -> Tuple[str, Operation]:
    monkey_name, operation_line = input.split(':')
    
    monkey_name = monkey_name.strip()
    operation_line = operation_line.strip().split()

    if len(operation_line) == 1:
        return monkey_name, Operation(lambda: int(operation_line[0]), None, None)
    
    if operation_line[1] == '+':
        return monkey_name, Operation(lambda x, y: x + y, operation_line[0], operation_line[2])
    elif operation_line[1] == '*':
        return monkey_name, Operation(lambda x, y: x * y, operation_line[0], operation_line[2])
    elif operation_line[1] == '-':
        return monkey_name, Operation(lambda x, y: x - y, operation_line[0], operation_line[2])
    elif operation_line[1] == '/':
        return monkey_name, Operation(lambda x, y: x / y, operation_line[0], operation_line[2])

def eval_monkey(monkey: Dict[str, Operation], monkey_name: str, already_evaluated: Dict[str, int]) -> int:
    if monkey_name in already_evaluated:
        return already_evaluated[monkey_name]
    
    arg1 = monkey[monkey_name].arg1
    arg2 = monkey[monkey_name].arg2

    if arg1 is None and arg2 is None:
        result = monkey[monkey_name].op()
        already_evaluated[monkey_name] = result

        return result

    if arg1 not in already_evaluated:
        already_evaluated[arg1] = eval_monkey(monkey, arg1, already_evaluated)
    
    if arg2 not in already_evaluated:
        already_evaluated[arg2] = eval_monkey(monkey, arg2, already_evaluated)
    
    result = monkey[monkey_name].op(already_evaluated[arg1], already_evaluated[arg2])
    already_evaluated[monkey_name] = result

    return result


if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    inputs = [parse_input(input) for input in inputs]
    
    monkeys = {input[0]: input[1] for input in inputs}

    print(eval_monkey(monkeys, 'root', {}))
