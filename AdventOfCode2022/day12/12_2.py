import os
import sys

from collections import defaultdict, namedtuple
from copy import deepcopy
from typing import Dict, List, Tuple, Callable, Union

Point = namedtuple("Point", "x y")


def read_input() -> List[str]:
    return [line for line in sys.stdin]


def convert_letter_to_height(c: str) -> int:
    if 'a' <= c <= 'z':
        return ord(c) - ord('a')
    elif c == 'S':
        return convert_letter_to_height('a')
    elif c == 'E':
        return convert_letter_to_height('z')


def split_input(lines: List[str]) -> List[List[int]]:
    return [[convert_letter_to_height(c) for c in line] for line in lines]


def is_position_inside(point: Point, bounds: Tuple[int, int]) -> bool:
    return 0 <= point.x < bounds[0] and 0 <= point.y < bounds[1]


def bfs(graph: List[List[int]], start=Point(0, 0), target=Point(0, 0)) -> int:
    queue = [(start, 0)]
    map_bounds = (len(graph), len(graph[0]))
    distances = {}

    visited = set()
    shortest_path = 1000000

    while len(queue) > 0:
        position, path = queue.pop(0)

        if not is_position_inside(position, map_bounds) or position in visited:
            continue
        
        if position == target:
            shortest_path = min(shortest_path, path)
        
        visited.add(position)

        for offset_x, offset_y in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            next_position = Point(position.x + offset_x, position.y + offset_y)

            if not is_position_inside(next_position, map_bounds):
                continue

            if heights[next_position.x][next_position.y] - heights[position.x][position.y] <= 1:
                queue.append((next_position, path + 1))

    return shortest_path

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    
    for i, line in enumerate(inputs):
        j = line.find('E')
        if j != -1:
            end = Point(i, j)
    
    heights = split_input(inputs)

    result = []
    for i, line in enumerate(heights):
        for j, height in enumerate(line):
            if height == 0:
                result.append(bfs(heights, Point(i, j), end))

    # print(bfs(heights, start, end))
    print(min(result))