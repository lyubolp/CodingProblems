class Solution:
    def canCompleteFrom(self, gas: List[int], cost: List[int], start: int) -> bool:
        current_gas = gas[start] - cost[start]
        current = start + 1
        if current >= len(gas):
                current = 0
                
        while current != start:
            current_gas += gas[current] - cost[current]
            if current_gas < 0:
                return False
            
            current = current + 1
            
            if current >= len(gas):
                current = 0
                
        return current_gas >= 0
        
        
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        possible_starts = [i for i in range(len(gas)) if gas[i] >= cost[i] and gas[i] != 0]
        
        for start in possible_starts:
            if self.canCompleteFrom(gas, cost, start):
                return start
        
        return -1

