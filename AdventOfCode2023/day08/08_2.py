import math
import sys

from itertools import cycle
from functools import reduce

direction_to_index = {'L': 0, 'R': 1}


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_nodes(lines: list[str]) -> dict[str, tuple[str, str]]:
    lines = [line.split('=') for line in lines]

    return {start.strip(): parse_destination(destination) for start, destination in lines}


def parse_destination(destination: str) -> tuple[str, str]:
    destination = destination.strip()

    destinations = destination.split(',')

    # Remove the ')'

    return destinations[0].strip()[1:], destinations[1].strip()[:-1]

if __name__ == "__main__":
    lines = read_input()

    sequence = lines[0].strip()

    nodes = parse_nodes(lines[2:])

    current_nodes = [node for node in nodes if node.endswith('A')]
    steps = 0

    directions = cycle(sequence)

    print(current_nodes)

    steps_from_all_start_nodes = []

    for current_node in current_nodes:
        steps = 0
        while not current_node.endswith('Z'):
            direction = next(directions)

            direction_index = direction_to_index[direction]

            current_node = nodes[current_node][direction_index]

            steps += 1

        steps_from_all_start_nodes.append(steps)

    result = math.lcm(*steps_from_all_start_nodes)

    print(int(result))
