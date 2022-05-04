class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        result = 0
        for num in count:
            if count[num] != 0:
                target = k - num
                
                if target in count:
                    to_remove = count[num] // 2 if target == num else min(count[num], count[target])

                    result += to_remove
                    count[num] -= to_remove
                    count[target] -= to_remove
        
        return result

