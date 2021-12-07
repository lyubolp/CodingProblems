#!/usr/bin/python3
import sys
from typing import List, Dict

def read_input() -> List[str]:
    return [line for line in sys.stdin]

def parse_input(lines: List[str]) -> List[int]:
    return [int(line.strip()) for line in lines[0].split(',')]

def decreaseBy(ages: List[int]) -> List[int]:
    ages.pop(0)
    ages.append(0)
    return ages

def day(ages: List[int]) -> List[int]:
    if ages[0] > 0:
        zeros = ages[0] 
        ages[0] -= zeros
        ages[9] += zeros
        ages[7] += zeros

    return decreaseBy(ages)

def days(ages: List[int], days: int) -> List[int]:
    for i in range(1, days+1):
        ages = day(ages)
    return ages
if __name__ == "__main__":
    all_ages = parse_input(read_input())

    ages = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for age in all_ages:
        ages[age] += 1
    
    ages = days(ages, 256)

    print(sum(ages))

