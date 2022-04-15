class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        arr = [(item, abs(item - x)) for item in arr]
        arr.sort(key=lambda x: (x[1], x[0]))
        
        arr = [item[0] for item in arr][:k]
        arr.sort()
        
        return arr

