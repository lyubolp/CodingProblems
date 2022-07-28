class Solution:
    def count_chars(self, s: str) -> dict:
        counter = {}
        
        for c in s:
            if c in counter:
                counter[c] += 1
            else:
                counter[c] = 1
        
        return counter
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = self.count_chars(s)
        t_count = self.count_chars(t)
        
        return s_count == t_count

