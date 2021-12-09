#!/usr/bin/python3
import sys
from typing import List

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def parse_input(lines: List[str]) -> List[List[int]]:
    return [[int(c) for c in line if c != '\n'] for line in lines]

def is_num_lowest(coordinates: List[List[int]], i: int, j: int) -> bool:
    neighbour_indexes = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]

    for target_i, target_j in neighbour_indexes:
        if 0 <= target_i < len(coordinates) and 0 <= target_j < len(coordinates[0]) and coordinates[i][j] >= coordinates[target_i][target_j]:
            return False
    
    return True

def calculate_risk_level(height: int) -> int:
    return height + 1

if __name__ == "__main__":
    coordinates = parse_input(read_input())
    print(coordinates)

    result = 0
    for i in range(len(coordinates)):
        for j in range(len(coordinates[0])):
            if is_num_lowest(coordinates, i, j):
                result += calculate_risk_level(coordinates[i][j])

    print(result)
