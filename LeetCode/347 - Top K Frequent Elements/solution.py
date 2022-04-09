class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        
        result = [(key, count[key]) for key in count]
        result = sorted(result, key=lambda x: x[1], reverse=True)[:k]
        result = [item[0] for item in result]
        
        return result

