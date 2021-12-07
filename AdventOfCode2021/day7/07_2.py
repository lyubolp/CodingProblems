#!/usr/bin/python3
import sys
from functools import reduce
from typing import List, Dict

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def parse_input(lines: List[str]) -> List[int]:
    return [int(line.strip()) for line in lines[0].split(',')]

def getNeededFuel(start, end) -> int:
    return sum(range(0, end - start + 1)) if start <= end else sum(range(0, start - end + 1))

if __name__ == "__main__":
    positions = parse_input(read_input())

    result = 10000000000
    for i in range(max(positions)):
        current_val = reduce(lambda acc, item: acc + getNeededFuel(item, i), positions, 0)
        result = min(result, current_val)

    print(result)