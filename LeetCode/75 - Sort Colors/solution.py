
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red = 0
        white = 0
        blue = 0

        for item in nums:
            if item == 0:
                red += 1
            elif item == 1:
                white += 1
            else:
                blue += 1

        for i in range(0, red):
            nums[i] = 0

        for i in range(red, red + white):
            nums[i] = 1

        for i in range(red+white, red + white + blue):
            nums[i] = 2

