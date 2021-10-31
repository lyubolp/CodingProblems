class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles_drank = 0
        empty_bottles = 0
        
        while numBottles > 0:
            if numBottles < numExchange:
                bottles_drank += numBottles
                empty_bottles += numBottles
                numBottles = 0
            else:
                numBottles -= numExchange
                bottles_drank += numExchange
                empty_bottles += numExchange
                
            
            if empty_bottles >= numExchange:
                numBottles += 1
                empty_bottles -= numExchange
            
            
        return bottles_drank

