class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 2 or arr[0] >= arr[1]:
            return False
        
        is_increasing = True
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            elif is_increasing and arr[i - 1] > arr[i]:
                is_increasing = False    
            if not is_increasing and arr[i - 1] < arr[i]:
                return False
        
        return not is_increasing

