#!/usr/bin/python3
import sys
from typing import List, Tuple

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def parse_input(lines: List[str]) -> List[List[int]]:
    return [[int(c) for c in s.strip()] for s in lines]

def increase_by_one(energy: List[List[int]]) -> List[List[int]]:
    return [[level + 1 for level in row] for row in energy]
    
def flash(energy: List[List[int]], flash_i: int, flash_j: int) -> List[List[int]]:
    energy[flash_i][flash_j] *= -1

    adj = [(1, 0), (-1, 0), (0, 1), (0, -1), (-1, 1), (-1, -1), (1, 1), (1, -1)]

    for offset_i, offset_j in adj:
        target_i = flash_i + offset_i
        target_j = flash_j + offset_j
        
        if 0 <= target_i < len(energy) and 0 <= target_j < len(energy[0]):
            energy[target_i][target_j] += 1
            if energy[target_i][target_j] > 9:
                energy = flash(energy, target_i, target_j)

    return energy

def clear_flashed(energy: List[List[int]]) -> List[List[int]]:
    return [[level if level > 0 else 0 for level in row] for row in energy]

def count_flashed(energy: List[List[int]]) -> int:
    return len([level for row in energy for level in row if level == 0])

def step(energy: List[List[int]]) -> Tuple[List[List[int]], int]:
    energy = increase_by_one(energy)

    for i in range(len(energy)):
        for j in range(len(energy[0])):
            if energy[i][j] > 9:
                energy = flash(energy, i, j)

    energy = clear_flashed(energy)
    return energy, count_flashed(energy)

if __name__ == "__main__":
    energy = parse_input(read_input())
    
    result = 0
    # print(f"energy before any steps: {energy}")
    steps = 195
    for i in range(195):
        energy, flashed_on_this_step = step(energy)
        # print(f"energy after step {i+1}: {energy}")
        result += flashed_on_this_step

    # print(f"energy after step {steps}: {energy}")
    print(result)
