import sys


def read_input() -> list[str]:
    return [line for line in sys.stdin]


def get_common_item(group: list[str]) -> str:
    first = set(group[0])
    second = set(group[1])
    third = set(group[2])

    return list(first & second & third)[0]


def calculate_priority(letter: str):
    if 'a' <= letter <= 'z':
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 27

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]
    groups = [inputs[i * 3 : (i+1) * 3] for i in range(len(inputs) // 3)]
    common_items = [get_common_item(group) for group in groups]
    common_items_priority = [calculate_priority(item) for item in common_items]

    print(sum(common_items_priority))
