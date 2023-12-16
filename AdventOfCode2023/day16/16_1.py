import sys
from collections import namedtuple

Point = namedtuple('Point', ['i', 'j'])
direction_to_offset = {'R': Point(0, 1), 'L': Point(0, -1), 'U': Point(-1, 0), 'D': Point(1, 0)}

mirror_direction_to_offset = {
    ('/', 'R'): 'U', ('/', 'L'): 'D', ('/', 'U'): 'R', ('/', 'D'): 'L',
    ('\\', 'R'): 'D', ('\\', 'L'): 'U', ('\\', 'U'): 'L', ('\\', 'D'): 'R',
}

splitter_direction_to_offsets = {
    ('-', 'R'): ['R'], ('-', 'L'): ['L'], ('-', 'U'): ['L', 'R'], ('-', 'D'): ['L', 'R'],
    ('|', 'R'): ['U', 'D'], ('|', 'L'): ['U', 'D'], ('|', 'U'): ['U'], ('|', 'D'): ['D']
}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_input(lines: list[str]) -> dict[Point, str]:
    return {Point(i, j): item for i, line in enumerate(lines) for j, item in enumerate(line)}


def bfs(grid: dict[Point, str], start: Point, bounds: Point) -> set[tuple[Point, str]]:
    queue = [(start, 'R')]

    visited = set()

    while len(queue) > 0:
        current = queue.pop(0)
        if current in visited:
            continue

        current_point, current_direction = current
        if not is_point_inside(current_point, bounds):
            continue

        visited.add(current)
        current_item = grid[current_point]

        if current_item == '.':
            new_point = offset_point(current_point, direction_to_offset[current_direction])
            queue.append((new_point, current_direction))
        elif current_item == '/' or current_item == '\\':
            new_direction = mirror_direction_to_offset[(current_item, current_direction)]
            new_point = offset_point(current_point, direction_to_offset[new_direction])
            queue.append((new_point, new_direction))
        elif current_item == '|' or current_item == '-':
            new_directions = splitter_direction_to_offsets[(current_item, current_direction)]
            for new_direction in new_directions:
                new_point = offset_point(current_point, direction_to_offset[new_direction])
                queue.append((new_point, new_direction))
        else:
            raise Exception("Unknown grid item")

    visited = set(point for point, _ in visited)
    return visited


def is_point_inside(point: Point, bounds: Point) -> bool:
    return 0 <= point.i < bounds.i and 0 <= point.j < bounds.j


def offset_point(point: Point, offset: Point) -> Point:
    return Point(point.i + offset.i, point.j + offset.j)


def display(visited: set[tuple[Point, str]], bounds: Point):
    for i in range(bounds.i):
        for j in range(bounds.j):
            if Point(i, j) in visited:
                print('#', end='')
            else:
                print('.', end='')
        print('')


if __name__ == "__main__":
    lines = read_input()

    grid = parse_input(lines)
    bounds = Point(len(lines), len(lines[0]))

    visited = bfs(grid, Point(0, 0), bounds)
    print(len(visited))
    # display(visited, bounds)
