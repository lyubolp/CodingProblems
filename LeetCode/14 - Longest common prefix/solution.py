class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lengths = [len(s) for s in strs]
        min_length = min(lengths)
        
        if min_length == 0:
            return ""
        i = 0
        for i in range(min_length):
            all_letters = [s[i] for s in strs]
            if not all(l == all_letters[0] for l in all_letters):
                i = i-1
                break
            
        return strs[0][:i+1]
        
