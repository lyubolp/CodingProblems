import sys


def read_input() -> list[str]:
    return [line.strip() for line in sys.stdin]


def parse_lines(lines: list[str]) -> list[tuple[str, int]]:
    return [(line[0], int(line[1:])) for line in lines]


def rotate_dial(dial: int, direction: str, amount: int) -> tuple[int, int]:
    full_rotations = amount // 100

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

    through_zero = full_rotations

    if direction == "L":
        if new_dial > dial and dial != 0 and new_dial != 0:
            through_zero += 1
    elif direction == "R":
        if new_dial < dial and dial != 0 and new_dial != 0:
            through_zero += 1

    return new_dial, through_zero


if __name__ == "__main__":
    lines = read_input()
    rotations = parse_lines(lines)

    # print(rotations)

    dial = 50
    password = 0
    for direction, amount in rotations:
        dial, through_zero = rotate_dial(dial, direction, amount)
        if dial == 0:
            password += 1
        password += through_zero
        print(f"{direction}{amount}, {dial}, {through_zero=}")

    print(password)
