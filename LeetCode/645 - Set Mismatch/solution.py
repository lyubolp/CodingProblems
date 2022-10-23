class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        actual = set(nums)
        expected = set(range(1, len(nums)+1))
        
        missing = list(expected - actual)[0]
        
        duplicate = Counter(nums).most_common(1)[0][0]
        
        return [duplicate, missing]

