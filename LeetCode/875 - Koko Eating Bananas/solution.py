class Solution:
    def timeToEatAll(self, piles: List[int], h: int, k: int) -> bool:
        return sum([ceil(item / k) for item in piles]) # O(p)
    
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 0
        end = max(piles)
        
        while start + 1 < end:
            mid = (end + start) // 2
            if self.timeToEatAll(piles, h, mid) > h: 
                start = mid
            else:
                end = mid
        
        return end
        
