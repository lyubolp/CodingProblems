class Solution:
    def build_counter(self, s: str) -> Dict[str, int]:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        
        return result
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_count = self.build_counter(s1)
        l1 = len(s1)
        s2_count = self.build_counter(s2[:l1])
        
        if s1_count == s2_count:
            return True
        
        for i in range(len(s1), len(s2)):
            to_remove = s2[i - l1]
            
            if s2_count[to_remove] == 1:
                del s2_count[to_remove]
            else:
                s2_count[to_remove] -= 1
                
            to_add = s2[i]
            if to_add not in s2_count:
                s2_count[to_add] = 1
            else:
                s2_count[to_add] += 1
            
            if s1_count == s2_count:
                return True
            
        
        return False

