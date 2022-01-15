class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxes = [max([candies[j] for j in range(len(candies)) if j != i]) for i in range(len(candies))]
        return [candies[i] + extraCandies >= maxes[i] for i in range(len(candies))]

