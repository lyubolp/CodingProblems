class Solution:
    def getArea(self, i, j, height) -> int:
        return (j - i) * min(height[i], height[j])
    def maxArea(self, height: List[int]) -> int:
        start = 0
        end = len(height) - 1
        
        result = (end - start) * min(height[start], height[end])
        current_result = 0
        while start + 1 < end:
            if height[start] <= height[end]:
                start += 1
            else:
                end -= 1
                
            current_result = (end - start) * min(height[start], height[end])
            result = max(result, current_result)
        
        return result

