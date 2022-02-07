class Solution:
    def count(self, s: str) -> Dict[str, int]:
        result = {}
        
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        
        return result 
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = self.count(s)
        t_count = self.count(t)
        
        for c in t:
            if c not in s_count or s_count[c] < t_count[c]:
                return c
        
        return ""

