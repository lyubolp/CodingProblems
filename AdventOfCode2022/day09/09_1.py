import os
import sys

from collections import namedtuple
from typing import Dict, List, Tuple

Point = namedtuple("Point", "x y")

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def split_input(input: List[str]) -> List[Tuple[str, int]]:
    results = [line.split() for line in input]
    return [(result[0], int(result[1])) for result in results]

def apply_step(head: Point, tail: Point, direction: str) -> Tuple[Point]:
    head = move_point(head, direction)

    if not are_head_and_tail_adjacent(head, tail):
        tail = tail_follow_head(head, tail, direction)
    
    return head, tail


def are_head_and_tail_adjacent(head: Point, tail: Point) -> bool:
    if head.x == tail.x or abs(head.x - tail.x) <= 1:
        return abs(head.y - tail.y) <= 1
    elif head.y == tail.y or abs(head.y - tail.y) <= 1:
        return abs(head.x - tail.x) <= 1

    return False


def move_point(point: Point, direction: str) -> Point:
    directions = {
        'R': (1, 0),
        'L': (-1, 0),
        'U': (0, 1),
        'D': (0, -1)
    }
    return Point(point.x + directions[direction][0], point.y + directions[direction][1])


def tail_follow_head(head: Point, tail: Point, direction: str) -> Point:
    if head.x == tail.x or head.y == tail.y:
        return move_point(tail, direction)
    
    if head.x > tail.x and head.y > tail.y:
        # up-right
        return move_point(move_point(tail, 'U'), 'R')
    elif head.x > tail.x and head.y < tail.y:
        # down-right
        return move_point(move_point(tail, 'D'), 'R')
    elif head.x < tail.x and head.y > tail.y:
        # up-left
        return move_point(move_point(tail, 'U'), 'L')
    elif head.x < tail.x and head.y < tail.y:
        # down-left
        return move_point(move_point(tail, 'D'), 'L')
    
    return tail

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    motions = split_input(inputs)

    head = Point(0, 0)
    tail = Point(0, 0)

    visited = set()
    for motion in motions:
        for i in range(motion[1]):
            head, tail = apply_step(head, tail, motion[0])
            visited.add(tail)
    
    print(len(visited))