import os
import sys

from collections import defaultdict
from typing import Dict, List, Tuple, Callable, Union


class Monkey:
    def __init__(self, id: int, items: List[int], operation: Tuple[str, Callable, Union[str, int]], test: int, throw_if_true: int, throw_if_false: int) -> None:
        self.id = id
        self.items = items
        self.operation = operation
        self.test = test
        self.throw_if_true = throw_if_true
        self.throw_if_false = throw_if_false

    def __str__(self):
        return f'Items = {self.items}, Operation = {self.operation}, Test = {self.test}, If true = {self.throw_if_true}, If false = {self.throw_if_false}'


    def single_turn(self, item) -> Tuple[int, int]:
        if self.operation[2] != 'old':
            worry_level = self.operation[1](item, self.operation[2])
        else:
            worry_level = self.operation[1](item, item)

        worry_level = worry_level // 3

        return worry_level, self.throw_if_true if self.test(worry_level) else self.throw_if_false
    
    def turn(self) -> List[Tuple[int, int]]:
        result = [self.single_turn(item) for item in self.items]
        self.items = []
        return result

def read_input() -> List[str]:
    return [line for line in sys.stdin]


def input_to_monkey(id: int, input: List[str]) -> Monkey:
    items = input[0].split(':')[1].strip().split(',')  #79, 98
    items = [int(item.strip()) for item in items]

    operation = input[1].split(':')[1].strip().split('=')[1].strip()  # new = old * 19

    first, operation, second = operation.split()

    if second != 'old':
        second = int(second)

    if operation == '+':
        operation = lambda x, y: x + y
    elif operation == '-':
        operation = lambda x, y: x - y
    elif operation == '*':
        operation = lambda x, y: x * y
    elif operation == '/':
        operation = lambda x, y: x / y
    

    test = int(input[2].split('by')[1].strip())
    test_fn = lambda x: x % test == 0
    
    throw_if_true = int(input[3].split('monkey')[1].strip())
    throw_if_false = int(input[4].split('monkey')[1].strip())

    return Monkey(id, items, (first, operation, second), test_fn, throw_if_true, throw_if_false)


def split_monkeys(lines: List[str]) -> List[List[str]]:
    result = []

    count = len([line for line in lines if line.startswith('Monkey')])

    for i in range(count):
        result.append(lines[(i * 7) + 1: ((i+1) * 7) + 1])
    
    return result



if __name__ == "__main__":
    inputs = [user_input.strip() for user_input in read_input()]

    splited_monkeys = list(enumerate(split_monkeys(inputs)))
    
    monkeys = [input_to_monkey(id, inputs) for id, inputs in splited_monkeys]
    
    inspection_count = defaultdict(lambda: 0)
    for round in range(20):
        for monkey in monkeys:
            result = monkey.turn()

            inspection_count[monkey.id] += len(result)
                
            for item, next_monkey_id in result:
                monkeys[next_monkey_id].items.append(item)
    
    most_active = sorted(inspection_count.values(), reverse=True)[:2]
    print(most_active[0] * most_active[1])
