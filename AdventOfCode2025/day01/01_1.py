import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_lines(lines: list[str]) -> list[tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in lines]


def rotate_dial(dial: int, direction: str, amount: int) -> int:
    amount = amount % 100
    new_dial = dial
    if direction == "L":
        new_dial -= amount
    elif direction == "R":
        new_dial += amount

    if new_dial < 0:
        new_dial += 100
    else:
        new_dial = new_dial % 100

    return new_dial


if __name__ == "__main__":
    lines = read_input()
    rotations = parse_lines(lines)

    # print(rotations)

    dial = 50
    password = 0
    for direction, amount in rotations:
        dial = rotate_dial(dial, direction, amount)
        if dial == 0:
            password += 1
        print(f"{direction}{amount}, {dial}")

    print(password)
