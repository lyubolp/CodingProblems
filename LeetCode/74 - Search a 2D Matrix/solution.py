class Solution:
    def search_rec(self, nums: List[List[int]], target: int, start: int, end: int):
        if end <= start:
            i = start // len(nums[0])
            j = start % len(nums[0])
            
            if nums[i][j] == target:
                return start
            else:
                return -1
        
        mid = (end - start) // 2 + start
        
        i = mid // len(nums[0])
        j = mid % len(nums[0])
        
        if nums[i][j] < target:
            return self.search_rec(nums, target, mid + 1, end)
        elif nums[i][j] > target:
            return self.search_rec(nums, target, start, mid - 1)
        else:
            return mid

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 1 and len(matrix[0]) == 1:
            return matrix[0][0] == target 
        
        return self.search_rec(matrix, target, 0, (len(matrix) * len(matrix[0])) - 1) != -1

