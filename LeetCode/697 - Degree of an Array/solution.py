class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = {}
        
        for i, num in enumerate(nums):
            if num not in count:
                count[num] = [1, [i]]
            else:
                count[num][0] += 1
                count[num][1].append(i)
            
        max_val = []
        degree = 0
        for key in count:
            current_degree = count[key][0]
            
            if current_degree > degree:
                degree = current_degree
                max_val = [key]
            elif current_degree == degree:
                max_val.append(key)
            
        result = 100000
        for val in max_val:
            current_len = max(count[val][1]) - min(count[val][1])
            result = min(current_len, result)
            
        return result + 1

