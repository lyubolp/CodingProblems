class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = {}
        
        for c in stones:
            if c not in count:
                count[c] = 1
            else:
                count[c] += 1

        return sum([count[jewel] for jewel in jewels if jewel in count])

