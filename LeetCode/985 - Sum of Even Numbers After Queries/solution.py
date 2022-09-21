class Solution:
    def calculate_change_to_sum(self, first: int, second: int) -> int:
        if first % 2 == 0 and second % 2 == 0:
            return second
        elif first % 2 == 0 and second % 2 != 0:
            return -first
        elif first % 2 != 0 and second % 2 != 0:
            return first + second
        else:
            return 0
        
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = sum(num for num in nums if num % 2 == 0)
        
        result = []
        for value, index in queries:
            even_sum += self.calculate_change_to_sum(nums[index], value)
            nums[index] += value
            
            result.append(even_sum)
            
        return result

