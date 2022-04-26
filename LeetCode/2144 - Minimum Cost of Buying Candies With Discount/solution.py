class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse=True)
        cost = [item for index, item in enumerate(cost) if index % 3 != 2]
        return sum(cost)

