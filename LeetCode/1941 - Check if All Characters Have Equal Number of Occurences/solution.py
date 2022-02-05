class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        count = {}
        for c in s:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
                
        counts = list(count.values())
        
        return all([counts[0] == item for item in counts])

