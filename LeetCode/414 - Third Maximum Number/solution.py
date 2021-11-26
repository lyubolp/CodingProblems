class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        distinct = []
        
        seen = set()
        
        for num in nums:
            if num not in seen:
                if len(distinct) < 3:
                    distinct.append(num)
                elif num > min(distinct):
                    index_of_min = distinct.index(min(distinct))
                    distinct.pop(index_of_min)
                    distinct.append(num)
                    
                
                seen.add(num)
            
        return min(distinct) if len(distinct) == 3 else max(distinct)

