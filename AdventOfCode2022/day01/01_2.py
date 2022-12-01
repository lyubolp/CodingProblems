import sys

def read_input() -> list[str]:
    return [line for line in sys.stdin]

if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]

    rations = []
    prev = 0
    for i, item in enumerate(inputs):
        if item == '':
            rations.append(inputs[prev:i])
            prev = i + 1
            
    rations.append(inputs[prev:])

    rations = sorted([sum(int(ration) for ration in rations_per_elf) for rations_per_elf in rations], reverse=True)

    print(sum(rations[:3]))

