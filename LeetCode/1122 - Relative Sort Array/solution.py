class Solution:
    def count(self, arr: List[int]) -> Dict[int, int]:
        result = {}
        
        for item in arr:
            if item in result:
                result[item] += 1
            else:
                result[item] = 1
        
        return result 
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = self.count(arr1)
        arr2_count = self.count(arr2)
        
        result = []
        
        for item in arr2_count:
            result += [item] * arr1_count[item]

        leftovers = []
        for item in arr1_count:
            if item not in arr2_count:
                leftovers += [item] * arr1_count[item]
        return result + sorted(leftovers)

