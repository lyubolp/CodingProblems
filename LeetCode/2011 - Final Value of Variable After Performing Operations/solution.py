class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        mapping = {'--X': -1, 'X--': -1, 'X++': 1, '++X': 1}
        
        return sum([mapping[operation] for operation in operations])

