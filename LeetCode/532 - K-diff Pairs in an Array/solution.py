class Solution:
    def find_target_nums_count(self, count: Dict[int, int], target: int, i: int, nums: List[int]) -> List[str]:
        return [str(sorted((nums[i], nums[j]))) for j in count[target] if i < j]
    def findPairs(self, nums: List[int], k: int) -> int:
        count = {}
        for i, num in enumerate(nums):
            if num in count:
                count[num].append(i)
            else:
                count[num] = [i]
                
        result = []
        for i, num in enumerate(nums):
            target1 = num - k
            target2 = num + k
            if target1 in count:
                result += self.find_target_nums_count(count, target1, i, nums)
                
            if target2 in count:
                result += self.find_target_nums_count(count, target2, i, nums)
        
        return len(set(result))

