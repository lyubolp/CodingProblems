class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count = {}
        
        for item in arr:
            if item in count:
                count[item] += 1
            else:
                count[item] = 1
        
        
        for item in arr:
            if count[item] == 1:
                if k == 1:
                    return item
                else:
                    k -= 1
        
        return ""

