class Solution:
    def count_sort(self, s: str) -> Dict[chr, int]:
        result = {}
        for c in s:
            if c in result:
                result[c] += 1
            else:
                result[c] = 1
        return result
    def findAnagrams(self, s: str, p: str) -> List[int]:
        
        result = []
        p_dict = self.count_sort(p)
        current = self.count_sort(s[:len(p)])
        
        if current == p_dict:
            result.append(0)
        
        j = 0
        for i in range(len(p), len(s)):
            c = s[i]
            current[s[j]] -= 1
            
            if current[s[j]] == 0:
                del current[s[j]]
            
            j += 1
            if c in current:
                current[c] += 1
            else:
                current[c] = 1
            
            if current == p_dict:
                result.append(j)
            
        return result

