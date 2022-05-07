class Solution:
    def findLucky(self, arr: List[int]) -> int:
        count = {}
        
        for num in arr:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        lucky_nums = [num for num in count if count[num] == num]
        
        return max(lucky_nums) if len(lucky_nums) > 0 else -1

