class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        result = [0] + [10001 for i in range(amount)]
    
        
        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0 and result[i - coin] != 10001:
                    result[i] = min(result[i], result[i-coin] + 1)
        
        return result[-1] if result[-1] != 10001 else -1

