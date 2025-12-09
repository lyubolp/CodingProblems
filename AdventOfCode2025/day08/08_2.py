import sys
import math

from collections import namedtuple, Counter
from functools import reduce

Point3D = namedtuple("Point3D", ["x", "y", "z"])


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_points(lines: list[str]) -> list[Point3D]:
    return [parse_point(line) for line in lines]


def parse_point(line: str) -> Point3D:
    x, y, z = line.split(",")

    return Point3D(int(x), int(y), int(z))


def calculate_distance(first: Point3D, second: Point3D) -> float:
    x = (first.x - second.x) ** 2
    y = (first.y - second.y) ** 2
    z = (first.z - second.z) ** 2
    return math.sqrt(x + y + z)


def get_all_distances(boxes: list[Point3D]) -> list[tuple[Point3D, Point3D, float]]:
    distances = [
        (first, second, calculate_distance(first, second))
        for i, first in enumerate(boxes)
        for second in boxes[i + 1 :]
        if first != second
    ]

    return list(sorted(distances, key=lambda item: item[2]))


def calculate_groups(circuits: dict[Point3D, int]) -> int:

    counts = Counter(circuits.values())

    groups = sorted(counts.values(), reverse=True)

    if len(groups) == 0:
        return 0

    return reduce(lambda acc, item: acc * item, groups[:3], 1)


if __name__ == "__main__":
    lines = read_input()
    boxes = parse_points(lines)

    distances = get_all_distances(boxes)

    next_circuit_id = 1
    circuits = {}
    distances_iter = iter(distances)

    boxes_in_circuits = 0

    last_pair = None
    while len(boxes) > boxes_in_circuits and calculate_groups(circuits) != 1:
        first, second, distance = next(distances_iter)

        if first not in circuits and second not in circuits:
            circuits[first] = next_circuit_id
            circuits[second] = next_circuit_id

            next_circuit_id += 1
            boxes_in_circuits += 2
        elif first in circuits and second not in circuits:
            circuits[second] = circuits[first]
            boxes_in_circuits += 1
        elif first not in circuits and second in circuits:
            circuits[first] = circuits[second]
            boxes_in_circuits += 1
        elif first in circuits and second in circuits:
            first_circuit = circuits[first]
            second_circuit = circuits[second]
            if first_circuit != second_circuit:
                for box, _id in circuits.items():
                    if _id == first_circuit or _id == second_circuit:
                        circuits[box] = next_circuit_id
            next_circuit_id += 1

        last_pair = first, second

    print(last_pair)

    result = last_pair[0].x * last_pair[1].x

    print(result)
