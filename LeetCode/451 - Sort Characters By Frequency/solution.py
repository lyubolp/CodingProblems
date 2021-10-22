class Solution:
    def frequencySort(self, s: str) -> str:
        count = {}
        rev_count = {}
        
        for c in s: 
            r = count[c] + 1 if c in count else 1
            count[c] = r
            
            if r in rev_count:
                rev_count[r].append(c)
            else:
                rev_count[r] = [c]
                
            
            if r - 1 in rev_count:
                if len(rev_count[r - 1]) == 1:
                    del rev_count[r - 1]
                else:
                    rev_count[r - 1].remove(c)
            
        result = []
        
        freq = list(rev_count.keys())
        freq.sort(reverse=True)
        
        for amount in freq:
            for letter in rev_count[amount]:
                result.append(letter * amount)
            
        return "".join(result)

