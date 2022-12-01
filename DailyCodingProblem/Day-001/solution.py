"""
2022-11-13
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""
def does_list_add_up_to_k(numbers: list[int], k: int) -> bool:
    numbers_seen_so_far = set()

    for number in numbers:
        target_number = k - number

        if target_number in numbers_seen_so_far:
            return True
        
        numbers_seen_so_far.add(number)
    
    return False

if __name__ == "__main__":
    print(does_list_add_up_to_k([10, 15, 3, 7], 17))  # True, because 10 + 7 = 17
    print(does_list_add_up_to_k([10, 15, 3, 7], 18))  # True, because 15 + 3 = 18
    print(does_list_add_up_to_k([10, 15, 3, 7], 19))  # False, because no two numbers that add up to 19
    print(does_list_add_up_to_k([10], 10)) # False, because there is no two numbers that add up to 19

