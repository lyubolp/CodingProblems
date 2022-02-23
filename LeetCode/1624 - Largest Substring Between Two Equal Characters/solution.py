class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        count = {}
        
        for i, c in enumerate(s):
            if c not in count:
                count[c] = [i]
            else:
                count[c].append(i)
                
        result = 0
        
        for key in count:
            if len(count[key]) > 1:
                distance = max(count[key]) - min(count[key])
                result = max(result, distance)
        
        return result - 1
        
