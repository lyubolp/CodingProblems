import sys


def read_input() -> list[str]:
    return [line for line in sys.stdin]


def split_input_into_compartments(input: str) -> tuple[str, str]:
    split_at = len(input) // 2
    return input[:split_at], input[split_at:]


def find_item_in_both_compartments(compartment: tuple[str, str]) -> str:
    first = set(compartment[0])
    second = set(compartment[1])

    return list(first & second)[0]


def calculate_priority(letter: str):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    rucksacks = [split_input_into_compartments(input) for input in inputs]
    items_in_both_compartments = [find_item_in_both_compartments(compartment) for compartment in rucksacks]
    priorities = [calculate_priority(item) for item in items_in_both_compartments]

    print(sum(priorities))
