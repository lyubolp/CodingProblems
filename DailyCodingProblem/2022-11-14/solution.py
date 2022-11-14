from functools import reduce
"""
2022-11-14
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?
"""

def transform_list(numbers: list[int]) -> list[int]:
    product = reduce(lambda acc, item: acc * item, numbers)

    return [product / number for number in numbers]


def get_product_of_list_without_index(numbers: list[int], index: int) -> int:
    return reduce(lambda acc, item: acc * item, numbers[:index] + numbers[index+1:])

def transform_list_no_division(numbers: list[int]) -> list[int]:
    return [get_product_of_list_without_index(numbers, i) for i in range(len(numbers))]

if __name__ == "__main__":
    print(transform_list([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
    print(transform_list([3, 2, 1]))  # [2, 3, 6]

    print(transform_list_no_division([1, 2, 3, 4, 5]))  # [120, 60, 40, 30, 24]
    print(transform_list_no_division([3, 2, 1]))  # [2, 3, 6]