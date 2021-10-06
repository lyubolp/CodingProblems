class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            i = abs(num) - 1
            
            if nums[i] < 0:
                result.append(abs(num))
            else:
                nums[i] *= -1

        return result

