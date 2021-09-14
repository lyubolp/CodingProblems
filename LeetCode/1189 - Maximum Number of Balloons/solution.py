class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {'b': 0, 'a': 0, 'l': 0, 'o': 0, 'n': 0}
        
        for c in text:
            if c in count:
                count[c] += 1
            else:
                count[c] = 1
        
        # balloon
        
        letters = [count['b'], count['a'], count['l'] // 2, count['o'] // 2, count['n']]
        
        return min(letters)

