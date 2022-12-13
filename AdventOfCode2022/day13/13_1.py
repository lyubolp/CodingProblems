import json
import os
import sys

from typing import Dict, List, Tuple, Callable, Union, Optional


def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input_into_pairs(inputs: List[str]) -> List[Tuple[str, str]]:
    inputs = [input for input in inputs if input != '']
    return [(inputs[(i*2)], inputs[(i*2 + 1)]) for i in range(len(inputs) // 2)]


def is_pair_in_right_order(first: str, second: str) -> bool:
    first = json.loads(first)
    second = json.loads(second)

    result = are_lists_in_right_order(first, second)

    return result


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
        
        if result is not None:
            return result
    
    return are_integers_in_right_order(len(first), len(second))


def are_integers_in_right_order(first: int, second: int) -> Optional[bool]:
    if first == second:
        return None
    
    return first < second


if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    inputs = split_input_into_pairs(inputs)

    indexes = [index + 1 for index, pair in enumerate(inputs) if is_pair_in_right_order(pair[0], pair[1])]
    
    print(sum(indexes))