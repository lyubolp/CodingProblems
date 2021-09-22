from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current = 0
        result = 0

        for num in nums:
            if num == 1:
                current += 1
            else:
                result = max(result, current)
                current = 0

        result = max(result, current)
        return result

if __name__ == "__main__":
    s = Solution()
    nums = [1,1,0,1,1,1]

    print(s.findMaxConsecutiveOnes(nums))