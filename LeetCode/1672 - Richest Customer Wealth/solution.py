class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_of_each_customer = [sum(acc) for acc in accounts]
        return max(wealth_of_each_customer)

