class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []
        result = []
        current = [str(nums[0])]
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i - 1]:
                current.append(str(nums[i]))
            else:
                if len(current) != 1:
                    result.append(f"{current[0]}->{current[-1]}")
                else:
                    result.append(current[0])
                current = [str(nums[i])]
        
        if len(current) != 1:
            result.append(f"{current[0]}->{current[-1]}")
        else:
            result.append(current[0])
            
        return result

