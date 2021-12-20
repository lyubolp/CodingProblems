class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        
        if len(arr) < 2:
            return []
        
        min_diff = arr[1] - arr[0]
        
        result = []
        for i in range(len(arr[:-1])):
            current_min = arr[i+1] - arr[i]
            if current_min < min_diff:
                min_diff = current_min
                result = [[arr[i], arr[i+1]]]
            elif current_min == min_diff:
                result.append([arr[i], arr[i+1]])
                
        return result

