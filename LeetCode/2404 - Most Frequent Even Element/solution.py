class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even = [num for num in nums if num % 2 == 0]
        
        if len(even) == 0:
            return -1
        even = sorted(even)
        counter = Counter(even)
        
        return counter.most_common()[0][0]

