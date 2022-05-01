#!/usr/bin/python3
import math
import sys

from collections import namedtuple
from functools import reduce
from typing import List, Tuple, Dict

Instruction = namedtuple('Instruction', ['name', 'operand1', 'operand2'])


def read_input() -> List[str]:
    return [line.strip() for line in sys.stdin if line != '\n']


def generate_instruction(line: str) -> Instruction:
    segments = line.split(' ')

    if len(segments) == 2:
        return Instruction(segments[0], segments[1], None)
    else:

        try:
            value = int(segments[2])
        except ValueError:
            value = segments[2]

    return Instruction(segments[0], segments[1], value)


def execute_instruction(instruction: Instruction, variables: Dict[str, int]) -> Dict[str, int]:
    a = instruction.operand1
    b = instruction.operand2

    if instruction.name == 'inp':
        variables[a] = b
    elif instruction.name == 'add':
        if type(b) == int:
            variables[a] += b
        else:
            variables[a] += variables[b]
    elif instruction.name == 'mul':
        if type(b) == int:
            variables[a] *= b
        else:
            variables[a] *= variables[b]
    elif instruction.name == 'div':
        if type(b) == int:
            variables[a] = variables[a] // b
        else:
            variables[a] = variables[a] // b
    elif instruction.name == 'mod':
        if type(b) == int:
            variables[a] %= b
        else:
            variables[a] %= variables[b]
    elif instruction.name == 'eql':
        if type(b) == int:
            variables[a] = 1 if variables[a] == b else 0
        else:
            variables[a] = 1 if variables[a] == variables[b] else 0
    else:
        raise ValueError("Invalid instruction")

    return variables


def is_number_valid(number: int, instructions: List[Instruction]) -> bool:
    variables = {
        'w': 0,
        'x': 0,
        'y': 0,
        'z': 0
    }

    for i in range(len(instructions)):
        if instructions[i].name == 'inp':
            length = int(math.log10(number))
            digit = int(number // pow(10, length)) if length > 1 else number
            instructions[i] = Instruction('inp', instructions[i].operand1, digit)
            number = number % pow(10, length)

    # variables = reduce(lambda acc, item: execute_instruction(item, acc), instructions, variables)
    for i, instruction in enumerate(instructions):
        variables = execute_instruction(instruction, variables)
        # print(i+1, instruction, variables)
    # print(variables)

    return variables['z'] == 0


if __name__ == "__main__":
    lines = read_input()
    instructions = [generate_instruction(line) for line in lines]

    max_number = 0

    for n in range(100000000000000, 11111111111111, -1):
        print(n)
        if '0' not in str(n) and is_number_valid(n, instructions):
            print(n)
            break

    # print(is_number_valid(13579246899999, instructions))
