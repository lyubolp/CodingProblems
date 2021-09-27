class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:    
        l = len(nums)
        left = [1]
        for i in range(1, l):
            left.append(left[i - 1] * nums[i - 1])
            
        right = [None] * l
        right[l - 1] = 1
                       
        for i in range(l-2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
            
        
        result = [left[i] * right[i] for i in range(l)]
            
        return result

