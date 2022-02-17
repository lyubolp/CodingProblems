class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack = []
        
        for item in candidates:
            if item <= target:
                stack.append(([item], item))
                
        
        result = []
        while len(stack) > 0:
            items, current_sum = stack.pop()
            
            if current_sum < target:
                for item in candidates:
                    stack.append((items + [item], current_sum + item))
            elif current_sum == target:
                result.append(items)
        
        result = [", ".join(str(i) for i in sorted(res)) for res in result]
        result = list(set(result))
        result = [item.split(', ') for item in result]
            
        return result

