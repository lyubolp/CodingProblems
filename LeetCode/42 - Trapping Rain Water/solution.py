from typing import List
class Solution:
    def calculateWaterArea(self, height: List[int], start: int, end: int) -> int:
        min_area = min(height[start], height[end])
        result = 0
        for i in range(start, end):
            current_block = min_area - height[i]
            result += current_block if current_block >= 0 else 0

        return result

    def trap(self, height: List[int]) -> int:
        water = 0

        i = 0
        while i < len(height) - 1:
            for j in range(i+1, len(height)):
                if height[i] <= height[j]:
                    water += self.calculateWaterArea(height, i, j)
                    print(i, j)
                    i = j - 1
                    break
            i += 1

        return water        

if __name__ == "__main__":
    height1 = [0,1,0,2,1,0,1,3,2,1,2,1]
    height2 = [4,2,0,3,2,5]
    height3 = [4, 2, 3]
    s = Solution()

    print(s.trap(height3))
    # 0
    # 0   0
    # 0 0 0
    # 0 0 0
