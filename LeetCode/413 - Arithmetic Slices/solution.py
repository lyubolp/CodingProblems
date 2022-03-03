class Solution:
    def is_list_arithmetic(self, nums: List[int]) -> int: 
        diff = nums[1] - nums[0]
        
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] != diff:
                return False
        
        return True
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        for i in range(len(nums) - 2):
            if self.is_list_arithmetic(nums[i:i+3]):
                diff = nums[i+1] - nums[i]
                result += 1
                for j in range(i+3, len(nums)):
                    if nums[j] - nums[j-1] == diff:
                        result += 1
                    else:
                        break
                    
        return result

