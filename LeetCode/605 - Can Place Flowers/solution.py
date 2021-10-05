class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for i, is_planted in enumerate(flowerbed):
            if is_planted == 1:
                if i > 0:
                    flowerbed[i - 1] = 2
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = 2
                    
        for i, is_planted in enumerate(flowerbed):
            if is_planted == 0:
                flowerbed[i] = 3
                if i > 0:
                    flowerbed[i - 1] = 2
                if i < len(flowerbed) - 1:
                    flowerbed[i + 1] = 2
                    
        return len([el for el in flowerbed if el == 3]) >= n

