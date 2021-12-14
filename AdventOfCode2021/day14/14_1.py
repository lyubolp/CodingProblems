#!/usr/bin/python3
import sys
from typing import List, Tuple, Dict, Set

def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def parse_input(lines: List[str]) -> Dict[str, str]:
    result = {}
    for line in lines:
        left, right = line.split("->")
        result[left.strip()] = right.strip()

    return result


def step(template: str, insertions: Dict[str, str]) -> str:
    pairs = [template[i:i+2] for i in range(len(template) - 1)]
    
    result = [apply_insertion(pair, insertions) for pair in pairs]

    # Joins the generated pairs back => ["AB", "BC", "CD"] should result in ABCD
    result = [result[0]] + [item[1:] for item in result[1:]]

    return "".join(result)


def apply_insertion(pair: str, insertion: Dict[str, str]) -> str:
    return pair[0] + insertion[pair] + pair[1] if pair in insertion else pair
    
def get_letter_count(template: str) -> Dict[str, int]:
    result = {}

    for c in template:
        if c in result:
            result[c] += 1
        else:
            result[c] = 1

    return result


if __name__ == "__main__":
    read_lines = read_input()

    polymer_template = read_lines[0]
    pair_insertion = parse_input(read_lines[1:])

    steps = 10
    for s in range(steps):
        polymer_template = step(polymer_template, pair_insertion)

    count = get_letter_count(polymer_template)

    print(max(count.values()) - min(count.values()))