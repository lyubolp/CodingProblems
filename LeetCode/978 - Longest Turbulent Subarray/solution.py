class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        is_lower = True
        result_lower = [0 for i in range(len(arr))]
        for i in range(len(arr) - 1):
            if (is_lower and arr[i] < arr[i+1]) or (not is_lower and arr[i] > arr[i+1]):
                result_lower[i] = result_lower[i-1] + 1

            is_lower = not is_lower
                
        is_lower = False
        result_higher = [0 for i in range(len(arr))]

        for i in range(len(arr) - 1):
            if (is_lower and arr[i] < arr[i+1]) or (not is_lower and arr[i] > arr[i+1]):
                result_higher[i] = result_higher[i-1] + 1

            is_lower = not is_lower
        return max(max(result_lower), max(result_higher)) + 1