#!/usr/bin/python3
import sys
from functools import reduce
from typing import List, Tuple

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

def bfs(coordinates: List[List[int]], start_i: int, start_j: int) -> List[Tuple[int, int]]:
    queue = []
    visited = set()

    offsets = [(-1, 0), (1, 0), (0, 1), (0, -1)]

    queue.append((start_i, start_j))

    while len(queue) > 0:
        current_x, current_y = queue.pop(0)

        for offset_x, offset_y in offsets:
            target_x = current_x + offset_x
            target_y = current_y + offset_y

            if 0 <= target_x < len(coordinates) and 0 <= target_y < len(coordinates[0]) \
                and coordinates[target_x][target_y] > coordinates[current_x][current_y] \
                and coordinates[target_x][target_y] != 9 \
                and (target_x, target_y) not in visited:
                queue.append((target_x, target_y))
            
        visited.add((current_x, current_y))

    return list(visited)



if __name__ == "__main__":
    coordinates = parse_input(read_input())
    print(coordinates)

    lowest_points = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates[0])):
            if is_num_lowest(coordinates, i, j):
                lowest_points.append((i, j))

    basin_sizes = []
    for low_point_i, low_point_j in lowest_points:
        basin_coordinates = bfs(coordinates, low_point_i, low_point_j)

        basin_sizes.append(len([coordinates[i][j] for i, j in basin_coordinates]))

    
    basin_sizes = sorted(basin_sizes, reverse=True)[:3]
    print(basin_sizes)
    print(reduce(lambda acc, item: acc * item, basin_sizes, 1))