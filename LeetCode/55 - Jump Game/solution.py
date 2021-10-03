class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i, n in enumerate(nums):
            if i > max_index:
                return False

            max_index = max(max_index, i + n)

        return True

