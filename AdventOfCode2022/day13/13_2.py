import json
import os
import sys

from functools import cmp_to_key
from typing import Dict, List, Tuple, Callable, Union, Optional


def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input_into_pairs(inputs: List[str]) -> List[Tuple[str, str]]:
    inputs = [input for input in inputs if input != '']
    return [(inputs[(i*2)], inputs[(i*2 + 1)]) for i in range(len(inputs) // 2)]


def is_pair_in_right_order(first: str, second: str) -> bool:
    first = json.loads(first)
    second = json.loads(second)

    return are_lists_in_right_order(first, second)


def are_lists_in_right_order(first: list, second: list) -> bool:
    result = None
    for i in range(min(len(first), len(second))):
        if isinstance(first[i], list) and isinstance(second[i], list):
            result = are_lists_in_right_order(first[i], second[i])
        elif isinstance(first[i], int) and isinstance(second[i], int):
            result = are_integers_in_right_order(first[i], second[i])
        elif isinstance(first[i], int) and isinstance(second[i], list):
            result = are_lists_in_right_order([first[i]], second[i])
        elif isinstance(first[i], list) and isinstance(second[i], int):
            result = are_lists_in_right_order(first[i], [second[i]])
        
        if result != 0:
            return result
    
    return are_integers_in_right_order(len(first), len(second))


def are_integers_in_right_order(first: int, second: int) -> int:
    if first < second:
        return -1
    elif first > second:
        return 1

    return 0

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    inputs = [input for input in inputs if input != '']

    first_divider = '[[2]]'
    second_divider = '[[6]]'

    inputs += [first_divider, second_divider]

    inputs = sorted(inputs, key=cmp_to_key(is_pair_in_right_order))

    # print('\n'.join(inputs))

    first_divider_index = inputs.index(first_divider) + 1
    second_divider_index = inputs.index(second_divider) + 1
    print(first_divider_index * second_divider_index)
    
