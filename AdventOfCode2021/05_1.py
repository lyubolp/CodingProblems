#!/usr/bin/python3
import sys
from typing import List, Tuple

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def convert_input_to_coordinates(input: str) -> List[Tuple[int, int]]:
    first, second = input.split("->")
    
    first_x, first_y = first.split(",")
    second_x, second_y = second.split(",")

    return [(int(first_x), int(first_y)), (int(second_x), int(second_y))]

def expand_coordinates(start: Tuple[int, int], end: Tuple[int, int]) -> List[Tuple[int, int]]:
    start_x, start_y = start
    end_x, end_y = end

    if start_x == end_x:
        return [(start_x, i) for i in range(min(start_y, end_y), max(start_y, end_y) + 1)]
    elif start_y == end_y:
        return [(i, start_y) for i in range(min(start_x, end_x), max(start_x, end_x) + 1)]
    else:
        return []

if __name__ == "__main__":
    lines = read_input()

    lines = [convert_input_to_coordinates(line.strip()) for line in lines]
    
    count = {}

    for line in lines:
        for point in expand_coordinates(line[0], line[1]):
            if point not in count:
                count[point] = 1
            else:
                count[point] += 1

    danger_points = [point for point in count if count[point] > 1]
    print(len(danger_points))