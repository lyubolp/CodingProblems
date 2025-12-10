import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_line(line: str) -> tuple[list[bool], list[list[int]], list[int]]:
    parts = line.split()

    lights = parse_lights(parts[0])
    buttons = parse_buttons(parts[1:-1])

    joltage = parse_joltage(parts[-1])

    return lights, buttons, joltage


def parse_buttons(raw_buttons: list[str]) -> list[list[int]]:
    result = [parse_button(raw_button) for raw_button in raw_buttons]

    return result


def parse_button(raw_button: str) -> list[int]:
    result = [int(item) for item in raw_button[1:-1].split(",")]

    return result


def parse_joltage(raw_joltage: str) -> list[int]:
    return [int(item) for item in raw_joltage[1:-1].split(",")]


def parse_lights(lights: str) -> list[bool]:
    return [light == "#" for light in lights[1:-1]]


def toggle_lights(target_lights: list[bool], buttons: list[list[int]]) -> int:
    start = [False] * len(target_lights)

    queue = [(start, 0)]

    while len(queue) > 0:
        current_lights, presses = queue.pop(0)

        if current_lights == target_lights:
            return presses

        for buttons_to_press in buttons:
            for button in buttons_to_press:
                current_lights[button] = not current_lights[button]
            queue.append((current_lights, presses + 1))

    return -1


if __name__ == "__main__":
    lines = read_input()

    parsed_lines = [parse_line(line) for line in lines]
    print(parsed_lines)
